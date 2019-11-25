import json
d = {"name": "TIM", "age": 16}
s=json.dumps(d)
print(s)
with open("text.txt","r") as file:
    print(json.load(file))
