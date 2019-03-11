import requests
import pymorphy2

infa = requests.get("https://horoomy-parsers.herokuapp.com/giveMePosts/sdam?num=5").text
print(infa)