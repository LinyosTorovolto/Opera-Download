import requests
import json
import random


dl_name = "opera"

def susAMOGUS(fi_name):
    with open(fi_name, "r") as fi:
        for line in fi.readlines():
            print(line)

with open("headers.json", "r") as fi:
    headers = json.load(fi)

with open("headers.json", "w") as fi:
    json.dump(headers,fi,indent=4)

idfk = random.randint(42493168, 92493168)

r = requests.get(f"https://net.geo.opera.com/opera/stable/windows?utm_tryagain=yes&utm_source=(direct)_via_opera_com&utm_medium=doc&utm_campaign=(direct)_via_opera_com_https&http_referrer=missing_via_opera_com&utm_site=opera_com&utm_lastpage=opera.com/download&dl_token={idfk}", headers=headers)

print(f"[+] Download status code: {r.status_code}")

if r.status_code == 200:
    print("[+] Opera.com thinks that this is not a bot")
    print("[+] Opera.com is stupid")

    with open(f"{dl_name}.exe", "wb") as fi:
        print("[+] Saving file...")
        fi.write(r.content)
    print("[+] SAVED SUCCSSFEFHNFKNSHDI")
    print("[+] Follow the download instructions bellow to get the exe")

else:
    print("[-] I am an idiot and made a stupid mistake in this program")
    print("[-] If you are from *** than follow the download instructions below and give me the zip file.")
    print("[-] The zip file will have an error log letting me figure out what went wrong and fix it")
    print("[-] Also call me an idiot pls while you are at it")




susAMOGUS("gaedoes10.txt")