import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'My User Agent 1.0',
    'From': 'youremail@domain.com'  # This is another valid field
}
url = "https://www.cian.ru/rent/flat/157907252/"
def getpics(url):
    all_images = []
    html = requests.get(url, headers=headers).text
    soup = BeautifulSoup(html, "html5lib")
    # infa = soup.find("div", {"class": "fotorama"})
    # images = infa.findAll("img")
    # for i in images:
    #     x = i.get("src")
    #     all_images.append(x)
    # metro_infa = soup.find("p", {"class": "objects_item_metro_prg"})
    return soup
print(getpics(url))
