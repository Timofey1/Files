import json
import requests

finalDict = {"99967": {"inOrOut": "out school", "datetime": {"date": "06.02.2017", "time": "13.05.07"}, "personInfo": {"first_name": "\u0422\u0438\u043c\u043e\u0444\u0435\u0439", "last_name": "\u041b\u0438", "id_staff": 7775}}, "99968": {"inOrOut": "out school", "datetime": {"date": "06.02.2017", "time": "13.05.19"}, "personInfo": {"first_name": "\u0413\u0435\u043e\u0440\u0433\u0438\u0439", "last_name": "\u0412\u043e\u043b\u043a\u043e\u0432", "id_staff": 7761}}}
sendJson = json.dumps(finalDict)
response = requests.post('http://int-school.herokuapp.com/post_info', json=sendJson)
print(response)
print(sendJson)