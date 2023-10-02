import requests
import os
from fake_useragent import UserAgent
import webbrowser
import re
import argparse
import threading
import chardet


def proxies(proxy):
    os.environ["http_proxy"] = f"{proxy}"
    os.environ["https_proxy"] = f"{proxy}"

ua = UserAgent()
headers = {
    'User-Agent': ua.chrome
}



def open_url(url, output_file,status_code,open_browser,detect_oss,default_status_code):
    try:
        session = requests.Session()
        if url.find("https") == -1:
            r = session.get(url, allow_redirects=False, timeout=5, headers=headers, verify=False)
        else:
            r = session.get(url, allow_redirects=False, timeout=5, headers=headers, verify=True)
        
        if default_status_code:
            print(f"{url}   {r.status_code}")
            if open_browser:
                webbrowser.open(url)
            with open(output_file,'a',encoding='utf-8') as f:
                f.write(f"{url}   {r.status_code}\n")

        if r.status_code == status_code:
            print(url)
            if open_browser:
                webbrowser.open(url)
            with open(output_file,'a',encoding='utf-8') as f:
                f.write(url + '\n')

        if detect_oss:
            text_to_search = r.text
            matches = ( 
        re.findall('access_key_id', text_to_search) or 
        re.findall('accesskeyid', text_to_search) or 
        re.findall('accesskeysecret', text_to_search) or 
        re.findall('accesskey', text_to_search) or 
        re.findall('oss_access',text_to_search) or 
        re.findall('apikey',text_to_search)
        )
        if matches:
            print(f"可能存在AK_KEY：{url}       {matches}")
            if open_browser:
                webbrowser.open(url)
            with open(output_file,'a',encoding='utf-8') as f:
                f.write(f"可能存在AK_KEY：{url}       {matches}\n")

        
    except Exception as e:
        pass
        # print(f"Error: {str(e)}")

def main():
    parser = argparse.ArgumentParser(description='Open URLs and check for OSS keys.') 
    parser.add_argument('-u', '--file', type=str, help='Enumerate files for urls')  
    parser.add_argument('-o', '--output', type=str, help='Specify the output file') 
    parser.add_argument('-sc','--status_code',type=int,default=200,help='Filter status code')
    parser.add_argument('-b','--browser',action='store_true',help='Open urls in a web browser')
    parser.add_argument('-oss','--detect_oss',action='store_true',help='Detect Oss keys')
    parser.add_argument('-d','--default_status_code',action='store_true',help='Default output status code for the current url') 
    parser.add_argument('--proxy',type=str,help='use proxies') 

    args = parser.parse_args() 

    if args.detect_oss or args.default_status_code:
        args.status_code = None
    url_file = args.file        
    output_file = args.output
    open_browser = args.browser
    
    # 使用 chardet 检测文件编码
    with open(url_file, 'rb') as file:
        encoding_info = chardet.detect(file.read())

    
    detected_encoding = encoding_info['encoding']

    
    file_lock = threading.Lock()

    def process_url(url):
        open_url(url, output_file, args.status_code, open_browser,args.detect_oss,args.default_status_code)
        if args.proxy:
            proxies(args.proxy)
        

    
    with open(url_file,'r',encoding=detected_encoding) as f:
        
        threads = []

        for line in f:
            url = line.strip()
        
            thread = threading.Thread(target=process_url,args=(url,))
            thread.start()
            threads.append(thread)

        
        for thread in threads:
            thread.join()

if __name__ == '__main__':
    print("")
    print("\033[1;92;40m  ____ \033[0m")
    print("\033[1;92;40m |_  _|  ________,,_____,\033[0m")
    print("\033[1;92;40m  |  |  / _____|||__ __|\033[0m")
    print("\033[1;92;40m  |  | / /     ||__| |__, \033[0m")
    print("\033[1;92;40m  |  | | |     ||__|_|__|\033[0m")
    print("\033[1;92;40m  |  | | |     ||_ | |\033[0m")
    print("\033[1;92;40m _|__|_| |_____||\\\| |\033[0m")
    print("\033[1;92;40m|______|_|_____// \\__|    V1.0 \033[0m")
    print("")
    print("")
    main()
