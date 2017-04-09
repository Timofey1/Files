import requests

headers = {'User-Agent':"Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_0 like Mac OS X; en-us) AppleWebKit/532.9 (KHTML, like Gecko) Version/4.0.5 Mobile/8A293 Safari/6531.22.7"}

url = "https://m.zara.com/ru/ru/search?filter=&searchTerm=%D1%84%D1%83%D1%82%D0%B1%D0%BE%D0%BB%D0%BA%D0%B0&isTopTerm=true"

html = requests.get(url, headers=headers).text
print(html)