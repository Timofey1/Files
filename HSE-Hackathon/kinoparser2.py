from bs4 import BeautifulSoup
import requests

url = "http://beregagent.ru/"

headers = {
    'User-Agent': 'My User Agent 1.0',
    'From': 'youremail@domain.com'  # This is another valid field
}

html = requests.get(url, headers=headers).text
print(html)