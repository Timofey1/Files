from bs4 import BeautifulSoup
import requests

url = "http://hypebeast.com/footwear"

html = requests.get(url).text

soup = BeautifulSoup(html, "lxml")  # На виндоусе вместо lxml надо поставить html5lib


post_boxes = soup.find_all('div', {'class': 'post-box'})
# Найти все теги div в которых параметр class равен post-box, на выходе будет Массив!!


article_title = article_soup.find('h1', {'class': 'title header-color-change-point'}).text  # .text - !!!
# Найти первый встречающийся тег h1 в котором class равен 'title header-color-change-point' и взять текст внутри тега

src = img.find('img').get('src')
# найти тег img и взять значение параметра src