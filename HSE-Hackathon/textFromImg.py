import requests
from bs4 import BeautifulSoup
import re

headers = {
    'User-Agent': 'My User Agent 1.0',
    'From': 'youremail@domain.com'  # This is another valid field
}

url = "https://www.avito.ru/moskva/kvartiry/1-k_kvartira_18_m_33_et._575430586"

def getsoup(url):
    html = requests.get(url).text
    soup = BeautifulSoup(html, "html5lib")
    return soup

soup = getsoup(url)

def getohone(soup):
    infa = soup.find("div", {"class": "item-phone-big-number"})
    print(infa)

getohone(soup)