import requests
for i in range(1):
    a = requests.get("https://browser-mining.contest.qctf.ru/shop", {"balance": 10000}).text
    print(a)