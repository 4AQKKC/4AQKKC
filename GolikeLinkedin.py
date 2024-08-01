
try :
    import requests
    import time
    import os 
    from art import *
    from colorama import Fore
    import time
    import json
    import sys
    import socket
    import random
    from tabulate import tabulate
    from datetime import datetime, timedelta
    from bs4 import BeautifulSoup
except ImportError:
    os.system("pip install requests")
    os.system("pip install tabulate")
    os.system("pip install art")
    os.system("pip install colorama")
def countdown(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        timeformat = 'Vui lòng chờ : {:02d} '.format(secs)
        print(timeformat, end='\r')
        time.sleep(1)
        time_sec -= 1

def LINKEDIN():
    checkaccount = requests.get('https://gateway.golike.net/api/linkedin-account',headers=headers).json()
    user_linkedin1 = []
    account_id1 = []
    totalMoney = 0
    STT = []
    STATUS =[]
    print('Các Tài Khoản Hoạt Động')
    i=1
    head = ["STT", "  Tài khoản","   Trạng Thái"]
    for data in checkaccount['data'] :
            usernametk = data['name']
            # print(str(i)+'.'+usernametk)
            user_linkedin1.append(data['name'])
            account_id1.append(data['id'])
            STT.append(i)
            STATUS.append(Fore.GREEN+"Hoạt động"+Fore.RED)
        # create header
            i=i+1
    table = zip(STT,user_linkedin1,STATUS)
    LIST=Fore.RED+tabulate(table, headers=head, tablefmt="grid",)   
    print(LIST)
    choose = int(input('Nhập Tài Khoản Chạy : '))
    os.system('cls' if os.name== 'nt' else 'clear')
    if choose >=1 or choose <= len(user_linkedin1) :
        user_LINKEDIN = user_linkedin1[choose-1:choose]
        account_id1 = account_id1[choose-1:choose]
        user_LINKEDIN= user_linkedin1[0] 
        account_id = account_id1[0]
        checkfile = os.path.isfile('COOKIELINKEDIN'+str(account_id)+'.txt')
        if checkfile == False:
            COOKIELINK = input(Fore.GREEN+'[+] COOKIE : ')
            createfile = open('COOKIELINKEDIN'+str(account_id)+'.txt','w')
            createfile.write(COOKIELINK)
            createfile.close()
            readfile = open('COOKIELINKEDIN'+str(account_id)+'.txt','r')
            COOKIELINK = readfile.read()
            readfile.close()
        else:
            readfile = open('COOKIELINKEDIN'+str(account_id)+'.txt','r')
            COOKIELINK = readfile.read()
            readfile.close()
        os.system('cls' if os.name== 'nt' else 'clear')
        banner = """
\033[1;33m██╗    ╔██╗ ██████╗  ████████╗ █████╗  █████╗ ██╗
\033[1;35m██║    ║██║ ██║    ██╚══██╔══╝██╔══██╗██╔══██╗██║
\033[1;36m██╔████╔██║ ██║    ██   ██║   ██║  ██║██║  ██║██║
\033[1;37m██║    ║██║ ██║    ██   ██║   ██║  ██║██║  ██║██║
\033[1;32m██║    ║██║ ██████╝     ██║   ╚█████╔╝╚█████╔╝███████╗
\033[1;98m╚═╝    ╚═╝╚═╝           ╚═╝    ╚════╝  ╚════╝ ╚══════╝
\033[97m╔════════════════════════════════════════════════════════╗
\033[1;97m║\033[1;33m *\033[1;97m TOOL NAME  \033[1;31m  : \033[1;91mTOOL \033[1;93mGOLIKE \033[1;97mLINKEDIN        \033[1;97m           ║\033[1;94m     
\033[1;97m║\033[1;33m * \033[1;97mLOCATINON \033[1;31m   : \033[1;33mVIỆT\033[1;91m NAM                     \033[1;97m         ║   \033[1;94m
\033[1;97m║\033[1;33m *\033[1;97m AUTHOR  \033[1;31m     : \033[1;97m☞HUONG\033[1;95m-\033[1;93mDEV🔫\033[1;97m☜          \033[1;97m               ║  \033[1;94m        
\033[1;97m║\033[1;33m *\033[1;97m ZALO    \033[1;31m     : \033[1;97m☞\033[1;31m0\033[1;37m3\033[1;36m6\033[1;35m2\033[1;34m1\033[1;33m6\033[1;33m6\033[1;34m8\033[1;35m6\033[1;37m3☜                \033[1;97m          ║  \033[1;94m  
\033[1;97m║\033[1;33m *\033[1;97m FACEBOOK \033[1;31m    : \033[1;32mi.urs.bin.python.TrinhHuong   \033[1;97m        ║   \033[1;94m         
\033[97m╚════════════════════════════════════════════════════════╝ \n
"""
        os.system("clear")
        for x in banner:
            print(x, end="")
        time.sleep(0.001)      
        print("\033[1;31mYouTube : \033[1;33mHuong \033[1;33mDev\033[1;32m")
        choose = int(input(Fore.RED+'Nhập Số Lượng Job : '))
        os.system('cls' if os.name== 'nt' else 'clear')
        banner = """
\033[1;33m██╗    ╔██╗ ██████╗  ████████╗ █████╗  █████╗ ██╗
\033[1;35m██║    ║██║ ██║    ██╚══██╔══╝██╔══██╗██╔══██╗██║
\033[1;36m██╔████╔██║ ██║    ██   ██║   ██║  ██║██║  ██║██║
\033[1;37m██║    ║██║ ██║    ██   ██║   ██║  ██║██║  ██║██║
\033[1;32m██║    ║██║ ██████╝     ██║   ╚█████╔╝╚█████╔╝███████╗
\033[1;98m╚═╝    ╚═╝╚═╝           ╚═╝    ╚════╝  ╚════╝ ╚══════╝
\033[97m╔════════════════════════════════════════════════════════╗
\033[1;97m║\033[1;33m *\033[1;97m TOOL NAME  \033[1;31m  : \033[1;91mTOOL \033[1;93mGOLIKE \033[1;97mLINKEDIN        \033[1;97m           ║\033[1;94m     
\033[1;97m║\033[1;33m * \033[1;97mLOCATINON \033[1;31m   : \033[1;33mVIỆT\033[1;91m NAM                     \033[1;97m         ║   \033[1;94m
\033[1;97m║\033[1;33m *\033[1;97m AUTHOR  \033[1;31m     : \033[1;97m☞HUONG\033[1;95m-\033[1;93mDEV🔫\033[1;97m☜          \033[1;97m               ║  \033[1;94m        
\033[1;97m║\033[1;33m *\033[1;97m ZALO    \033[1;31m     : \033[1;97m☞\033[1;31m0\033[1;37m3\033[1;36m6\033[1;35m2\033[1;34m1\033[1;33m6\033[1;33m6\033[1;34m8\033[1;35m6\033[1;37m3☜                \033[1;97m          ║  \033[1;94m  
\033[1;97m║\033[1;33m *\033[1;97m FACEBOOK \033[1;31m    : \033[1;32mi.urs.bin.python.TrinhHuong   \033[1;97m        ║   \033[1;94m         
\033[97m╚════════════════════════════════════════════════════════╝ \n
"""
    
        os.system("clear")
        for x in banner:
            print(x, end="")
        time.sleep(0.001)
        print("\033[1;31mYouTube : \033[1;33mHuong \033[1;33mDev\033[1;32m")
        DELAY = int(input(Fore.RED+'Nhập Delay Nhập Job : '))
        for i in range(choose):
                url2 = 'https://gateway.golike.net/api/advertising/publishers/linkedin/jobs?account_id='+str(account_id)+'&data=null'
                checkurl2 = ses.get(url2,headers=headers).json()
                if checkurl2['status'] ==200:
                    linkjob = []
                    linkjob = str(checkurl2['data']['link'])
                    lenjob = len(checkurl2['data']['link'])
                    ads_id = checkurl2['data']['id']
                    object_id = checkurl2['data']['object_id']
                    type = checkurl2['data']['type']
                    countdown(DELAY)
                    if type == 'follow':
                        haeaders = {
                            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                            'accept-language': 'vi,en-US;q=0.9,en;q=0.8',
                            'cache-control': 'max-age=0',
                            'cookie':COOKIELINK ,
                            'priority': 'u=0, i',
                            'referer': 'https://app.golike.net/',
                            'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
                            'sec-ch-ua-mobile': '?0',
                            'sec-ch-ua-platform': '"Windows"',
                            'sec-fetch-dest': 'document',
                            'sec-fetch-mode': 'navigate',
                            'sec-fetch-site': 'same-origin',
                            'sec-fetch-user': '?1',
                            'upgrade-insecure-requests': '1',
                            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
                            }

                        response = requests.get(str(linkjob),  headers=haeaders).text
                        if 'li:fsd_company' not in response and 'identityDashProfilesByMemberIdentity&quot;:{&quot;*elements&quot;:[&quot;urn:li:fsd_profile:' not in response:
                                    json_data2 = {
                                    'account_id': account_id,
                                    'ads_id': ads_id,
                                     }
                                    url = 'https://gateway.golike.net/api/advertising/publishers/linkedin/complete-jobs'
                                    check = requests.post(url,headers=headers,json=json_data2).json()
                                    if check['success']==True:
                                            prices =check['data']['prices']
                                            # print(Fore.CYAN+'['+str(i)+']'+'|'+Fore.WHITE+type+'|'+Fore.GREEN+str(ads_id)+' | '+Fore.YELLOW+str(prices)+'VND'+'|'+Fore.BLUE+"SUCCESS")
                                            totalMoney += prices
                                        # In ra thông tin
                                            print(Fore.CYAN + '[' + str(i) + ']' + '|' +
                                            Fore.WHITE + type + '|' +
                                            Fore.GREEN + str(ads_id) + ' | ' +
                                            Fore.YELLOW + str(prices) + ' vnd' + ' | ' +
                                            Fore.BLUE + "success" + ' | Total: ' + Fore.GREEN + str(totalMoney) + ' vnd |')
                                    else:
                                            skipjob = 'https://gateway.golike.net/api/advertising/publishers/linkedin/skip-jobs'
                                            PARAMS = {
                                            'ads_id' : ads_id,
                                            'account_id' : account_id,
                                            'object_id' : object_id ,
                                            }
                                            checkskipjob = ses.post(skipjob,params=PARAMS).json()
                                            if checkskipjob['status'] == 200:
                                                message = checkskipjob['message']
                                                print(Fore.RED+str(message))
                                                PARAMSr = {
                                                'ads_id' : ads_id,
                                                'account_id' : account_id,
                                                'object_id' : object_id ,
                                                }
                        else:
                            json_data = {
                            'patch': {
                                '$set': {
                                    'following': True,
                                },
                            },
                            }
                            json_data2 = {
                                    'account_id': account_id,
                                    'ads_id': ads_id,
                                }
                            try:
                                crft =  COOKIELINK.split('JSESSIONID="')[1].split('"')[0],
                                try:
                                    headersX = {
                                    'accept': 'application/vnd.linkedin.normalized+json+2.1',
                                    'accept-language': 'vi,en-US;q=0.9,en;q=0.8',
                                    'content-type': 'application/json; charset=UTF-8',
                                    'cookie': COOKIELINK,
                                    'csrf-token': COOKIELINK.split('JSESSIONID="')[1].split('"')[0],
                                    'origin': 'https://www.linkedin.com',
                                    'priority': 'u=1, i',
                                    'referer': 'https://www.linkedin.com/company/chatplayground-ai/posts/?feedView=all',
                                    'sec-fetch-dest': 'empty',
                                    'sec-fetch-mode': 'cors',
                                    'sec-fetch-site': 'same-origin',
                                    'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1',
                                    'x-li-lang': 'en_US',
                                    'x-li-page-instance': 'urn:li:page:companies_company_posts_index;7952eddd-435c-428e-9587-a2dd19a42e2f',
                                    'x-li-pem-metadata': 'Voyager - Organization - Member=organization-follow',
                                    'x-li-track': '{"clientVersion":"1.13.19938","mpVersion":"1.13.19938","osName":"web","timezoneOffset":7,"timezone":"Asia/Bangkok","deviceFormFactor":"DESKTOP","mpName":"voyager-web","displayDensity":1.5625,"displayWidth":2400,"displayHeight":1350}',
                                    'x-restli-protocol-version': '2.0.0',
                                    }

                                    ID = response.split('li:fsd_company:')[1].split('&')[0]
                                    follow = requests.post('https://www.linkedin.com/voyager/api/feed/dash/followingStates/urn:li:fsd_followingState:urn:li:fsd_company:'+ID,headers=headersX,json=json_data)
                                    url = 'https://gateway.golike.net/api/advertising/publishers/linkedin/complete-jobs'
                                    time.sleep(2)
                                    check = requests.post(url,headers=headers,json=json_data2).json()
                                    if check['success']==True:
                                            prices =check['data']['prices']
                                            totalMoney += prices
                                        # In ra thông tin
                                            print(Fore.CYAN + '[' + str(i) + ']' + '|' +
                                            Fore.WHITE + type + '|' +
                                            Fore.GREEN + str(ads_id) + ' | ' +
                                            Fore.YELLOW + str(prices) + ' vnd' + ' | ' +
                                            Fore.BLUE + "success" + ' | Total: ' + Fore.GREEN + str(totalMoney) + ' vnd |')
                                    else:
                                            skipjob = 'https://gateway.golike.net/api/advertising/publishers/linkedin/skip-jobs'
                                            PARAMS = {
                                            'ads_id' : ads_id,
                                            'account_id' : account_id,
                                            'object_id' : object_id ,
                                            }
                                            checkskipjob = ses.post(skipjob,params=PARAMS).json()
                                            if checkskipjob['status'] == 200:
                                                message = checkskipjob['message']
                                                print(Fore.RED+str(message))
                                                PARAMSr = {
                                                'ads_id' : ads_id,
                                                'account_id' : account_id,
                                                'object_id' : object_id ,
                                                }
                                except IndexError:
                                    headersY = {
                                    'accept': 'application/vnd.linkedin.normalized+json+2.1',
                                    'accept-language': 'vi,en-US;q=0.9,en;q=0.8',
                                    'content-type': 'application/json; charset=UTF-8',
                                    'cookie':COOKIELINK,
                                    'csrf-token': COOKIELINK.split('JSESSIONID="')[1].split('"')[0],
                                    'origin': 'https://www.linkedin.com',
                                    'priority': 'u=1, i',
                                    'referer': 'https://www.linkedin.com/in/noman-chaudhary-52031148/',
                                    'sec-fetch-dest': 'empty',
                                    'sec-fetch-mode': 'cors',
                                    'sec-fetch-site': 'same-origin',
                                    'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1',
                                    'x-li-lang': 'en_US',
                                    'x-li-page-instance': 'urn:li:page:d_flagship3_profile_view_base;I6RhpcMURWuRvBmeIhl5BQ==',
                                    'x-li-pem-metadata': 'Voyager - Follows=follow-action,Voyager - Profile Actions=topcard-primary-follow-action-click',
                                    'x-li-track': '{"clientVersion":"1.13.19938","mpVersion":"1.13.19938","osName":"web","timezoneOffset":7,"timezone":"Asia/Bangkok","deviceFormFactor":"DESKTOP","mpName":"voyager-web","displayDensity":1.5625,"displayWidth":2400,"displayHeight":1350}',
                                    'x-restli-protocol-version': '2.0.0',
                                    }
                                    try:
                                        ID = response.split('identityDashProfilesByMemberIdentity&quot;:{&quot;*elements&quot;:[&quot;urn:li:fsd_profile:')[1].split('&')[0]
                                        follow =  requests.post('https://www.linkedin.com/voyager/api/feed/dash/followingStates/urn:li:fsd_followingState:urn:li:fsd_profile:'+ID,headers=headersY,json=json_data) 
                                        time.sleep(2)
                                        url = 'https://gateway.golike.net/api/advertising/publishers/linkedin/complete-jobs'
                                        check = requests.post(url,headers=headers,json=json_data2).json()
                                        if check['success']==True:
                                                prices =check['data']['prices']
                                                totalMoney += prices
                                        # In ra thông tin
                                                print(Fore.CYAN + '[' + str(i) + ']' + '|' +
                                                Fore.WHITE + type + '|' +
                                                Fore.GREEN + str(ads_id) + ' | ' +
                                                Fore.YELLOW + str(prices) + ' vnd' + ' | ' +
                                                Fore.BLUE + "success" + ' | Total: ' + Fore.GREEN + str(totalMoney) + ' vnd |')
                                        else:
                                                skipjob = 'https://gateway.golike.net/api/advertising/publishers/linkedin/skip-jobs'
                                                PARAMS = {
                                                'ads_id' : ads_id,
                                                'account_id' : account_id,
                                                'object_id' : object_id ,
                                                }
                                                checkskipjob = ses.post(skipjob,params=PARAMS).json()
                                                if checkskipjob['status'] == 200:
                                                    message = checkskipjob['message']
                                                    print(Fore.RED+str(message))
                                                    PARAMSr = {
                                                    'ads_id' : ads_id,
                                                    'account_id' : account_id,
                                                    'object_id' : object_id ,
                                                    }
                                    except IndexError:
                                        print('COOKIE DIE')
                                        os.remove('COOKIELINKEDIN'+str(account_id)+'.txt')
                                        return 0
                            except IndexError:
                                try:
                                    headersX = {
                                    'accept': 'application/vnd.linkedin.normalized+json+2.1',
                                    'accept-language': 'vi,en-US;q=0.9,en;q=0.8',
                                    'content-type': 'application/json; charset=UTF-8',
                                    'cookie': COOKIELINK,
                                    'csrf-token': COOKIELINK.split('JSESSIONID=')[1].split(';')[0],
                                    'origin': 'https://www.linkedin.com',
                                    'priority': 'u=1, i',
                                    'referer': 'https://www.linkedin.com/company/chatplayground-ai/posts/?feedView=all',
                                    'sec-fetch-dest': 'empty',
                                    'sec-fetch-mode': 'cors',
                                    'sec-fetch-site': 'same-origin',
                                    'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1',
                                    'x-li-lang': 'en_US',
                                    'x-li-page-instance': 'urn:li:page:companies_company_posts_index;7952eddd-435c-428e-9587-a2dd19a42e2f',
                                    'x-li-pem-metadata': 'Voyager - Organization - Member=organization-follow',
                                    'x-li-track': '{"clientVersion":"1.13.19938","mpVersion":"1.13.19938","osName":"web","timezoneOffset":7,"timezone":"Asia/Bangkok","deviceFormFactor":"DESKTOP","mpName":"voyager-web","displayDensity":1.5625,"displayWidth":2400,"displayHeight":1350}',
                                    'x-restli-protocol-version': '2.0.0',
                                    }

                                    ID = response.split('li:fsd_company:')[1].split('&')[0]
                                    follow = requests.post('https://www.linkedin.com/voyager/api/feed/dash/followingStates/urn:li:fsd_followingState:urn:li:fsd_company:'+ID,headers=headersX,json=json_data)
                                    time.sleep(2)
                                    url = 'https://gateway.golike.net/api/advertising/publishers/linkedin/complete-jobs'
                                    check = requests.post(url,headers=headers,json=json_data2).json()
                                    if check['success']==True:
                                            prices =check['data']['prices']
                                            totalMoney += prices
                                        # In ra thông tin
                                            print(Fore.CYAN + '[' + str(i) + ']' + '|' +
                                            Fore.WHITE + type + '|' +
                                            Fore.GREEN + str(ads_id) + ' | ' +
                                            Fore.YELLOW + str(prices) + ' vnd' + ' | ' +
                                            Fore.BLUE + "success" + ' | Total: ' + Fore.GREEN + str(totalMoney) + ' vnd |')
                                    else:
                                            skipjob = 'https://gateway.golike.net/api/advertising/publishers/linkedin/skip-jobs'
                                            PARAMS = {
                                            'ads_id' : ads_id,
                                            'account_id' : account_id,
                                            'object_id' : object_id ,
                                            }
                                            checkskipjob = ses.post(skipjob,params=PARAMS).json()
                                            if checkskipjob['status'] == 200:
                                                message = checkskipjob['message']
                                                print(Fore.RED+str(message))
                                                PARAMSr = {
                                                'ads_id' : ads_id,
                                                'account_id' : account_id,
                                                'object_id' : object_id ,
                                                }
                                except IndexError:
                                    headersY = {
                                    'accept': 'application/vnd.linkedin.normalized+json+2.1',
                                    'accept-language': 'vi,en-US;q=0.9,en;q=0.8',
                                    'content-type': 'application/json; charset=UTF-8',
                                    'cookie':COOKIELINK,
                                    'csrf-token': COOKIELINK.split('JSESSIONID=')[1].split(';')[0],
                                    'origin': 'https://www.linkedin.com',
                                    'priority': 'u=1, i',
                                    'referer': 'https://www.linkedin.com/in/noman-chaudhary-52031148/',
                                    'sec-fetch-dest': 'empty',
                                    'sec-fetch-mode': 'cors',
                                    'sec-fetch-site': 'same-origin',
                                    'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1',
                                    'x-li-lang': 'en_US',
                                    'x-li-page-instance': 'urn:li:page:d_flagship3_profile_view_base;I6RhpcMURWuRvBmeIhl5BQ==',
                                    'x-li-pem-metadata': 'Voyager - Follows=follow-action,Voyager - Profile Actions=topcard-primary-follow-action-click',
                                    'x-li-track': '{"clientVersion":"1.13.19938","mpVersion":"1.13.19938","osName":"web","timezoneOffset":7,"timezone":"Asia/Bangkok","deviceFormFactor":"DESKTOP","mpName":"voyager-web","displayDensity":1.5625,"displayWidth":2400,"displayHeight":1350}',
                                    'x-restli-protocol-version': '2.0.0',
                                    }
                                    try:
                                        ID = response.split('identityDashProfilesByMemberIdentity&quot;:{&quot;*elements&quot;:[&quot;urn:li:fsd_profile:')[1].split('&')[0]
                                        follow =  requests.post('https://www.linkedin.com/voyager/api/feed/dash/followingStates/urn:li:fsd_followingState:urn:li:fsd_profile:'+ID,headers=headersY,json=json_data) 
                                        time.sleep(2)
                                        url = 'https://gateway.golike.net/api/advertising/publishers/linkedin/complete-jobs'
                                        check = requests.post(url,headers=headers,json=json_data2).json()
                                        if check['success']==True:
                                                prices =check['data']['prices']
                                                totalMoney += prices
                                        # In ra thông tin
                                                print(Fore.CYAN + '[' + str(i) + ']' + '|' +
                                                Fore.WHITE + type + '|' +
                                                Fore.GREEN + str(ads_id) + ' | ' +
                                                Fore.YELLOW + str(prices) + ' vnd' + ' | ' +
                                                Fore.BLUE + "success" + ' | Total: ' + Fore.GREEN + str(totalMoney) + ' vnd |')
                                        else:
                                                skipjob = 'https://gateway.golike.net/api/advertising/publishers/linkedin/skip-jobs'
                                                PARAMS = {
                                                'ads_id' : ads_id,
                                                'account_id' : account_id,
                                                'object_id' : object_id ,
                                            
                                                }
                                                checkskipjob = ses.post(skipjob,params=PARAMS).json()
                                                if checkskipjob['status'] == 200:
                                                    message = checkskipjob['message']
                                                    print(Fore.RED+str(message))
                                                    PARAMSr = {
                                                    'ads_id' : ads_id,
                                                    'account_id' : account_id,
                                                    'object_id' : object_id ,
                                                    
                                                    }
                                    except IndexError:
                                        print('COOKIE DIE')
                                        os.remove('COOKIELINKEDIN'+str(account_id)+'.txt')
                                        return 0
                    elif type == 'like':
                        try:
                            crft =  COOKIELINK.split('JSESSIONID')[1].split(';')[0],

                            headersL = {
                                'accept': 'application/vnd.linkedin.normalized+json+2.1',
                                'accept-language': 'vi,en-US;q=0.9,en;q=0.8',
                                'content-type': 'application/json; charset=UTF-8',
                                'cookie': COOKIELINK,
                                'csrf-token': COOKIELINK.split('JSESSIONID=')[1].split(';')[0],
                                'origin': 'https://www.linkedin.com',
                                'priority': 'u=1, i',
                                'referer': 'https://www.linkedin.com/feed/update/urn:li:activity:7219700822467575808/',
                                'sec-fetch-dest': 'empty',
                                'sec-fetch-mode': 'cors',
                                'sec-fetch-site': 'same-origin',
                                'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1',
                                'x-li-lang': 'en_US',
                                # 'x-li-page-instance': 'urn:li:page:d_flagship3_detail_base;T3jRBiYHTZqgLY+qsIgtkg==',
                                'x-li-track': '{"clientVersion":"1.13.20142","mpVersion":"1.13.20142","osName":"web","timezoneOffset":7,"timezone":"Asia/Bangkok","deviceFormFactor":"DESKTOP","mpName":"voyager-web","displayDensity":1.5625,"displayWidth":2400,"displayHeight":1350}',
                                'x-restli-protocol-version': '2.0.0',
                            }

                            params = {
                                'action': 'execute',
                                'queryId': 'voyagerSocialDashReactions.b731222600772fd42464c0fe19bd722b',
                            }

                            json_data = {
                                'variables': {
                                    'entity': {
                                        'reactionType': 'LIKE',
                                    },
                                    'threadUrn': 'urn:li:activity:'+str(object_id),
                                },
                                'queryId': 'voyagerSocialDashReactions.b731222600772fd42464c0fe19bd722b',
                                'includeWebMetadata': True,
                            }

                            response = requests.post(
                                'https://www.linkedin.com/voyager/api/graphql',
                                params=params,
                                headers=headersL,
                                json=json_data,
    
                            )
                        except IndexError:
                            headersN = {
                                'accept': 'application/vnd.linkedin.normalized+json+2.1',
                                'accept-language': 'vi,en-US;q=0.9,en;q=0.8',
                                'content-type': 'application/json; charset=UTF-8',
                                'cookie': COOKIELINK,
                                'csrf-token': COOKIELINK.split('JSESSIONID="')[1].split('"')[0],
                                'origin': 'https://www.linkedin.com',
                                'priority': 'u=1, i',
                                'referer': 'https://www.linkedin.com/feed/update/urn:li:activity:7219700822467575808/',
                                'sec-fetch-dest': 'empty',
                                'sec-fetch-mode': 'cors',
                                'sec-fetch-site': 'same-origin',
                                'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1',
                                'x-li-lang': 'en_US',
                                # 'x-li-page-instance': 'urn:li:page:d_flagship3_detail_base;T3jRBiYHTZqgLY+qsIgtkg==',
                                'x-li-track': '{"clientVersion":"1.13.20142","mpVersion":"1.13.20142","osName":"web","timezoneOffset":7,"timezone":"Asia/Bangkok","deviceFormFactor":"DESKTOP","mpName":"voyager-web","displayDensity":1.5625,"displayWidth":2400,"displayHeight":1350}',
                                'x-restli-protocol-version': '2.0.0',
                            }

                            params = {
                                'action': 'execute',
                                'queryId': 'voyagerSocialDashReactions.b731222600772fd42464c0fe19bd722b',
                            }

                            json_data = {
                                'variables': {
                                    'entity': {
                                        'reactionType': 'LIKE',
                                    },
                                    'threadUrn': 'urn:li:activity:'+str(object_id),
                                },
                                'queryId': 'voyagerSocialDashReactions.b731222600772fd42464c0fe19bd722b',
                                'includeWebMetadata': True,
                            }

                            response = requests.post(
                                'https://www.linkedin.com/voyager/api/graphql',
                                params=params,
                                headers=headersN,
                                json=json_data,
        
                            )
                        json_data2 = {
                                'account_id': account_id,
                                'ads_id': ads_id,
                            }
                        time.sleep(2)
                        url = 'https://gateway.golike.net/api/advertising/publishers/linkedin/complete-jobs'
                        check = requests.post(url,headers=headers,json=json_data2).json()
                        if check['success']==True:
                                prices =check['data']['prices']
                                totalMoney += prices
                                        # In ra thông tin
                                print(Fore.CYAN + '[' + str(i) + ']' + '|' +
                                Fore.WHITE + type + '| ' +
                                Fore.GREEN + str(ads_id) + ' | ' +
                                Fore.YELLOW + str(prices) + ' vnd' + ' | ' +
                                Fore.BLUE + "success" + ' | Total: ' + Fore.GREEN + str(totalMoney) + ' vnd |')
                        else:
                                skipjob = 'https://gateway.golike.net/api/advertising/publishers/linkedin/skip-jobs'
                                PARAMS = {
                                'ads_id' : ads_id,
                                'account_id' : account_id,
                                'object_id' : object_id ,
                                }
                                checkskipjob = ses.post(skipjob,params=PARAMS).json()
                                if checkskipjob['status'] == 200:
                                    message = checkskipjob['message']
                                    print(Fore.RED+str(message))
                                    PARAMSr = {
                                    'ads_id' : ads_id,
                                    'account_id' : account_id,
                                    'object_id' : object_id ,
                                    'async': 'true',
                                    'data': 'null',
                                    'type': type,
                                    }   
                else:        
                    print(checkurl2['message'])
                    countdown(15)
 
 
def LIST():
    banner = """
\033[1;33m██╗    ╔██╗ ██████╗  ████████╗ █████╗  █████╗ ██╗
\033[1;35m██║    ║██║ ██║    ██╚══██╔══╝██╔══██╗██╔══██╗██║
\033[1;36m██╔████╔██║ ██║    ██   ██║   ██║  ██║██║  ██║██║
\033[1;37m██║    ║██║ ██║    ██   ██║   ██║  ██║██║  ██║██║
\033[1;32m██║    ║██║ ██████╝     ██║   ╚█████╔╝╚█████╔╝███████╗
\033[1;98m╚═╝    ╚═╝╚═╝           ╚═╝    ╚════╝  ╚════╝ ╚══════╝
\033[97m╔════════════════════════════════════════════════════════╗
\033[1;97m║\033[1;33m *\033[1;97m TOOL NAME  \033[1;31m  : \033[1;91mTOOL \033[1;93mGOLIKE \033[1;97mLINKEDIN        \033[1;97m           ║\033[1;94m     
\033[1;97m║\033[1;33m * \033[1;97mLOCATINON \033[1;31m   : \033[1;33mVIỆT\033[1;91m NAM                     \033[1;97m         ║   \033[1;94m
\033[1;97m║\033[1;33m *\033[1;97m AUTHOR  \033[1;31m     : \033[1;97m☞HUONG\033[1;95m-\033[1;93mDEV🔫\033[1;97m☜          \033[1;97m               ║  \033[1;94m        
\033[1;97m║\033[1;33m *\033[1;97m ZALO    \033[1;31m     : \033[1;97m☞\033[1;31m0\033[1;37m3\033[1;36m6\033[1;35m2\033[1;34m1\033[1;33m6\033[1;33m6\033[1;34m8\033[1;35m6\033[1;37m3☜                \033[1;97m          ║  \033[1;94m  
\033[1;97m║\033[1;33m *\033[1;97m FACEBOOK \033[1;31m    : \033[1;32mi.urs.bin.python.TrinhHuong   \033[1;97m        ║   \033[1;94m         
\033[97m╚════════════════════════════════════════════════════════╝ \n
"""

    os.system("clear")
    for x in banner:
        print(x, end="")
        time.sleep(0.001)

    print("\033[1;31mYouTube : \033[1;33mHuong \033[1;33mDev\033[1;32m")
    print("\033[1;32mNhập \033[1;31m1 \033[1;33mđể vào \033[1;34mTool Linkedin\033[1;33m")

checkfile = os.path.isfile('user.txt')

if checkfile == False:
    AUTHUR = input(Fore.GREEN+'[+]''NHAP Authorization : ')
    createfile = open('user.txt','w')
    createfile.write(AUTHUR)
    createfile.close()
    readfile = open('user.txt','r')
    file = readfile.read()
    readfile.close()
else:
    readfile = open('user.txt','r')
    file = readfile.read()
    readfile.close()
ses = requests.Session()
User_Agent=random.choice(open("useragent.txt","r").readline().splitlines())
headers = {'Accept-Language':'vi,en-US;q=0.9,en;q=0.8',
            'Referer':'https://app.golike.net/',
            'Sec-Ch-Ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
            'Sec-Ch-Ua-Mobile':'?0',
            'Sec-Ch-Ua-Platform':"Windows",
            'Sec-Fetch-Dest':'empty',
            'Sec-Fetch-Mode':'cors',
            'Sec-Fetch-Site':'same-site',
            'T' : 'VFZSamQwOUVSVEpQVkVFd1RrRTlQUT09',
            'User-Agent':User_Agent,
            "Authorization" : file,
            'Content-Type':'application/json;charset=utf-8'            
}

url1 = 'https://gateway.golike.net/api/users/me'
checkurl1 = ses.get(url1,headers=headers).json()
    #user
if checkurl1['status']== 200 :
        print('DANG NHAP THANH CONG')
        time.sleep(3)
        os.system('cls' if os.name== 'nt' else 'clear')
        banner = """
\033[1;33m██╗    ╔██╗ ██████╗  ████████╗ █████╗  █████╗ ██╗
\033[1;35m██║    ║██║ ██║    ██╚══██╔══╝██╔══██╗██╔══██╗██║
\033[1;36m██╔████╔██║ ██║    ██   ██║   ██║  ██║██║  ██║██║
\033[1;37m██║    ║██║ ██║    ██   ██║   ██║  ██║██║  ██║██║
\033[1;32m██║    ║██║ ██████╝     ██║   ╚█████╔╝╚█████╔╝███████╗
\033[1;98m╚═╝    ╚═╝╚═╝           ╚═╝    ╚════╝  ╚════╝ ╚══════╝
\033[97m╔════════════════════════════════════════════════════════╗
\033[1;97m║\033[1;33m *\033[1;97m TOOL NAME  \033[1;31m  : \033[1;91mTOOL \033[1;93mGOLIKE \033[1;97mLINKEDIN        \033[1;97m           ║\033[1;94m     
\033[1;97m║\033[1;33m * \033[1;97mLOCATINON \033[1;31m   : \033[1;33mVIỆT\033[1;91m NAM                     \033[1;97m         ║   \033[1;94m
\033[1;97m║\033[1;33m *\033[1;97m AUTHOR  \033[1;31m     : \033[1;97m☞HUONG\033[1;95m-\033[1;93mDEV🔫\033[1;97m☜          \033[1;97m               ║  \033[1;94m        
\033[1;97m║\033[1;33m *\033[1;97m ZALO    \033[1;31m     : \033[1;97m☞\033[1;31m0\033[1;37m3\033[1;36m6\033[1;35m2\033[1;34m1\033[1;33m6\033[1;33m6\033[1;34m8\033[1;35m6\033[1;37m3☜                \033[1;97m          ║  \033[1;94m  
\033[1;97m║\033[1;33m *\033[1;97m FACEBOOK \033[1;31m    : \033[1;32mi.urs.bin.python.TrinhHuong   \033[1;97m        ║   \033[1;94m         
\033[97m╚════════════════════════════════════════════════════════╝ \n
"""

        os.system("clear")
        for x in banner:
            print(x, end="")
            time.sleep(0.001)

        print("\033[1;31mYouTube : \033[1;33mHuong \033[1;33mDev\033[1;32m")
        print(Fore.BLUE + '1.Tool Golike Mobile')
        choose = int(input(Fore.WHITE + 'Nhập Lựa Chọn : '))
        if choose == 1 :
            username = checkurl1['data']['username']
            coin = checkurl1['data']['coin']
            user_id = checkurl1['data']['id']
            print('________________________________________________________')
            print(Fore.GREEN+'[+] USERNAME : '+Fore.YELLOW+username)
            print(Fore.GREEN+'[+] TIEN : '+Fore.YELLOW+str(coin))
            print(Fore.RED+'_________________________________________________________')
            LIST()
            print(Fore.RED+'Nhập 2 Để Xóa Authorization Hiện Tại')
            choose = int(input(Fore.WHITE+'Nhập Lựa Chọn : '))
            if choose == 1:
                os.system('cls' if os.name== 'nt' else 'clear')
                banner = """
\033[1;33m██╗    ╔██╗ ██████╗  ████████╗ █████╗  █████╗ ██╗
\033[1;35m██║    ║██║ ██║    ██╚══██╔══╝██╔══██╗██╔══██╗██║
\033[1;36m██╔████╔██║ ██║    ██   ██║   ██║  ██║██║  ██║██║
\033[1;37m██║    ║██║ ██║    ██   ██║   ██║  ██║██║  ██║██║
\033[1;32m██║    ║██║ ██████╝     ██║   ╚█████╔╝╚█████╔╝███████╗
\033[1;98m╚═╝    ╚═╝╚═╝           ╚═╝    ╚════╝  ╚════╝ ╚══════╝
\033[97m╔════════════════════════════════════════════════════════╗
\033[1;97m║\033[1;33m *\033[1;97m TOOL NAME  \033[1;31m  : \033[1;91mTOOL \033[1;93mGOLIKE \033[1;97mLINKEDIN        \033[1;97m           ║\033[1;94m     
\033[1;97m║\033[1;33m * \033[1;97mLOCATINON \033[1;31m   : \033[1;33mVIỆT\033[1;91m NAM                     \033[1;97m         ║   \033[1;94m
\033[1;97m║\033[1;33m *\033[1;97m AUTHOR  \033[1;31m     : \033[1;97m☞HUONG\033[1;95m-\033[1;93mDEV🔫\033[1;97m☜          \033[1;97m               ║  \033[1;94m        
\033[1;97m║\033[1;33m *\033[1;97m ZALO    \033[1;31m     : \033[1;97m☞\033[1;31m0\033[1;37m3\033[1;36m6\033[1;35m2\033[1;34m1\033[1;33m6\033[1;33m6\033[1;34m8\033[1;35m6\033[1;37m3☜                \033[1;97m          ║  \033[1;94m  
\033[1;97m║\033[1;33m *\033[1;97m FACEBOOK \033[1;31m    : \033[1;32mi.urs.bin.python.TrinhHuong   \033[1;97m        ║   \033[1;94m         
\033[97m╚════════════════════════════════════════════════════════╝ \n
"""

                os.system("clear")
                for x in banner:
                    print(x, end="")
                    time.sleep(0.001)

                print("\033[1;31mYouTube : \033[1;33mHuong \033[1;33mDev\033[1;32m")
                ip = requests.get('https://api.ipify.org?format=json').json()
                print(Fore.RED+'IP CUA BAN : '+Fore.GREEN+str(ip['ip']))
                LINKEDIN()
            elif choose == 2:
                 os.remove('user.txt')
else:
    print(Fore.RED+'DANG NHAP THAT BAI')
    os.remove('user.txt')











    
