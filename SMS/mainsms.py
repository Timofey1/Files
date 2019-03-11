import requests
import json
import hashlib


class SMS:
    headers = {'Content-type': 'application/x-www-form-urlencoded'}

    def __init__(self, p, a):
        self.project = p  # Имя проекта
        self.api_key = a  # API-ключ
        self.url = 'http://mainsms.ru/api/'

    # выполнение запроса
    def doRequest(self, rqData, url):

        rqData['project'] = self.project
        l = []
        sign = ''

        for i in rqData:
            l.append(str(rqData[i]))
        l.sort()

        for element in l:
            sign = sign + str(element) + ';'

        sign = sign + str(self.api_key)

        sign = hashlib.sha1(sign.encode("utf-8")).hexdigest()
        sign = hashlib.md5(sign.encode("utf-8")).hexdigest()

        rqData['sign'] = sign

        r = requests.get(self.url + url, headers=self.headers, params=rqData)
        # print r.url		# Когда что-то идёт не по плану, можно посмотреть GET запрос (через браузер)
        # r = requests.post(self.url+url, headers=self.headers, data=rqData)	#POST работал только с одиночными SMS

        print(r.text)

        ansver = json.loads(r.text)
        return ansver

    # Одиночные смс
    def sendSMS(self, recipients, message, sender='', run_at='', test=0):  # шлём SMS
        rqData = {
            "recipients": recipients,
            "message" : message,
            "test" 		: test
        }
        if sender != '':
            rqData['sender' ] =sender

        # если указана дата-время (формат  "дд.мм.гггг чч:мм")
        if run_at != '':
            rqData['run_at' ] =run_at
        return self.doRequest(rqData, 'message/send')

    def getBalance(self):		# узнаём баланс
        rqData = {}
        return self.doRequest(rqData, 'message/balance')

    def messagePrice(self, recipients, message):		# узнаём цену сообщений
        rqData = {
            "recipients": recipients,
            "message" 	: message,
            "sender" 	: self.sender
        }
        return self.doRequest(rqData, 'message/price')

    def info(self, phones ):	# узнаём информацию о номерах
        rqData = {"phones" : phones}
        return self.doRequest(rqData, 'message/info')

    def statusSMS(self, messages_id):	# узнаём статус SMS
        rqData = {"messages_id" : messages_id}
        return self.doRequest(rqData, 'message/status')

    # Рассылки
    def create(self, include, message, exclude=0, sender='', run_at='', slowtime='', slowsize='', name='', test=0):	# Создание смс рассылки
        rqData = {
            "include"	: include,
            "message"	: message
        }
        if sender != '':
            rqData['sender' ] =sender

        if slowtime != '':
            rqData['slowtime' ] =slowtime

        if slowsize != '':
            rqData['slowsize' ] =slowsize

        if name != '':
            rqData['name' ] =name

        if run_at != '':
            rqData['run_at' ] =run_at

        if exclude != 0:
            rqData['exclude' ] =exclude

        if test != 0:
            rqData['test' ] =test

        return self.doRequest(rqData, 'sending/create')

    def groups(self, type):	# Запрос групп
        rqData = {"type" : type}
        return self.doRequest(rqData, 'sending/groups')

    def status(self, id):	# Запрос статуса рассылки
        rqData = {"id" : id}
        return self.doRequest(rqData, 'sending/status')

