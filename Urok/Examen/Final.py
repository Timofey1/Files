# coding=utf-8
import requests
import json
from firebase import firebase
firebase_url = "https://school-92a93.firebaseio.com/"


class Pogoda:
    sity_name = ""
    localtime = ""
    temp_c = ""
    text = ""

    def __init__(self, sity_name, localtime, temp_c, text):
        self.sity_name = sity_name
        self.localtime = localtime
        self.temp_c = temp_c
        self.text = text

sity = ["Novosibirsk", "Moscow", "Saint Petersburg", "Yekaterinburg", "Samara", "Omsk", "Kazan", "Chelyabinsk", "Ufa", "Volgograd"]

all_infa = []

for i in sity:
    url = "https://api.apixu.com/v1/current.json?key=4e6b94078deb4170b2c174438172805&q=" + i
    jsn = requests.get(url).text
    try:
        fin_json = json.loads(jsn)
    except json.decoder.JSONDecodeError:
        print("HREF ERROR")
        break
    if "location" in fin_json:
        infa = fin_json["location"]
        if "name" in infa:
            sity_name = infa["name"]
        if "localtime" in infa:
            localtime = infa["localtime"]
    if "current" in fin_json:
        infa = fin_json["current"]
        if "temp_c" in infa:
            temp_c = infa["temp_c"]
        if "condition" in infa:
            infa_text = infa["condition"]
            if "text" in infa_text:
                text = infa_text["text"]

    all_infa.append(Pogoda(sity_name, localtime, temp_c, text))
# print(all_infa)


def uploadinfo():
    db = firebase.FirebaseApplication(firebase_url)
    for gorod in all_infa:
        # print(gorod.__dict__)
        db.post("/infBySity", gorod.__dict__)

    # print(db.get("/infBySity", None))

