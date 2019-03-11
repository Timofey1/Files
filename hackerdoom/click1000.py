import requests
from bs4 import BeautifulSoup

url = "https://click1000.training.hackerdom.ru/"

for i in range(1000):
    html = requests.get(url).text
    soup = BeautifulSoup(html, "html5lib")
    href = soup.find("a").get("href")
    print(href)
    url = "https://click1000.training.hackerdom.ru/" + href
print(requests.get(url).text)