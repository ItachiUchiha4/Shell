import re
import requests
import requests

#f=open("File.txt","r")
f = open('c2.txt','r').read().split('\n')


headers = {
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/63.0.3239.84 Chrome/63.0.3239.84 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
}

for line in f: 
    try:
        response = requests.get("http://"+str(line),headers=headers,timeout=3).text
        if ".exe" in response:
            print("[+] Check  " + line)
        else:
            pass
    except Exception as e:
        print("May be time out ")
        pass
