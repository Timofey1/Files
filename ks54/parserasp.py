import requests
from bs4 import BeautifulSoup

groupName  = "2-КС11-3"
global days
days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница"]



def getInfoZamena(groupName):
    ur = "https://www.ks54.ru/Студенту/Расписание_On-Line?group="
    url = ur + groupName
    html = requests.get(url).text
    soup = BeautifulSoup(html, "html5lib")
    Tabs = soup.findAll("table", {"class": "bcol w100"})
    try:
        mainTab = Tabs[1]
    except:
        print("Замен нет")

    tds = mainTab.findAll("td")
    for i in tds:
        print(i.text)


def getInfo(groupName):
    day = ""
    js = {"Понедельник":[], "Вторник":[],"Среда":[],"Четверг":[],"Пятница":[]}
    ur = "https://www.ks54.ru/Студенту/Расписание_On-Line?group="
    url = ur + groupName
    html = requests.get(url).text
    soup = BeautifulSoup(html, "html5lib")
    mainTab = soup.find("table", {"class": "bcol w100"})
    tds = mainTab.findAll("td")

    for elem in tds:
        if elem.text in days:
            day = elem.text
            continue
        else:
            js[day].append(elem)

    return js


def oneDayRasp(js, elem):
    print(elem)
    for i in range(len(js[elem])):
        if js[elem][i].text in ["1", "2", "3", "4"]:
            print()
            c=i
            print(js[elem][i].text)
        elif c == i - 4 or c == i - 8:
            print(js[elem][i].text)
            print("----------------------")
        else:
            print(js[elem][i].text)


def allweek(js):
    for elem in days:
        print(elem)
        for i in range(len(js[elem])):
            if js[elem][i].text in ["1", "2", "3", "4"]:
                print()
                c = i
                print(js[elem][i].text)
            elif c == i - 4 or c == i - 8:
                print(js[elem][i].text)
                print("----------------------")
            else:
                print(js[elem][i].text)

    return


#json = getInfo("2-ИСП11-2")
#neDayRasp(json, "Понедельник")
#allweek(json)
















