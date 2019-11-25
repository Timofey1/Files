from bs4 import BeautifulSoup
import requests
import html5lib

text = requests.get("http://terrikon.com/football/russia/championship/").text

soup = BeautifulSoup(text,"html5lib")
table = soup.find('table',{"class":"gameresult"})
x=table.findAll("tr")

for tr in x:
    teams=tr.findAll('td',{'class':'team'})
    for j in teams:
        print(j.text)
    print(tr.find('td',{'class':'date'}).text)