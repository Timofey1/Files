# -*- coding: utf-8 -*-
import requests
import hashlib
import re

class SMS:
    def __init__(self, l, p):
        self.login = l
        self.psw = p
        self.url = "http://smsc.ru/"

    def doRequest(self, rqData, url):
        rqData["login"] = self.login
        psw = self.psw
        m = hashlib.md5()
        m.update(psw.encode('utf-8'))
        rqData["psw"] = m.hexdigest()
        print(rqData)
        #r = requests.get(self.url + url, params=rqData)
        #print(r.text)
        #return r.text

    def sendSMS(self, phone, message,sender=''):
        if self.checkPhone(phone) != 0:
            rqData = {"phones": phone, "mes": message, "charset": "utf-8", "fmt": "3"}
            if sender != "":
                rqData['sender'] = sender
            return self.doRequest(rqData, "sys/send.php")
        else:
            return "Wrong type Number"

    def balance(self):
        rqData = {"fmt": "3"}
        return self.doRequest(rqData, "sys/balance.php")

    def history(self,cnt="1", start="", end="", phone=""):
        rqData = {"get_messages": "1","cnt":cnt,"fmt": "3"}
        if cnt != "1":
            rqData["cnt"] = str(cnt)
        if phone != "":
            if self.checkPhone(phone) != 0:
                rqData["phone"] = phone
            else:
                print("Error")
                return "Wrong type phone"
        if start != "":
            if self.checkData(start) != 0:
                rqData["start"] = start
            else:
                print("Error")
                return "Wrong type start"
        if end != "":
            if self.checkData(end) != 0:
                rqData["end"] = end
            else:
                print("Error")
                return "Wrong type end"
        return self.doRequest(rqData,"sys/get.php")

    def getStatistic(self, start, end, mycur="1"):
        rqData = {"get_stat": "1", "start": start, "end": end, "mucur": mycur}
        if self.checkData(start) != 0 and self.checkData(end) != 0:
            return self.doRequest(rqData, "sys/get.php")
        else:
            print("Error")
            return "Error"


    def checkPhone(self, phone, rqData):
        if re.match(r'7[0-9]{10}', phone) and len(phone) == 11:
            return phone
        else:
            return 0

    def checkData(self, data):
        if re.match(r'[0-9]{2}\.[0-9]{2}\.[0-9]{4}',data) and len(data) == 10:
            return data
        else:
            return 0




sms = SMS("horoomy","h0r00my")
#sms.sendSMS("79175905310", "привет")
#sms.balance()
#sms.history()
sms.getStatistic("11.11.1111","22.22.2222")