import requests
#with open('text.txt', 'w')as outfile:
    #outfile.write(requests.get("http://api.vk.com/method/users.get?user_ids=timbeshkurov&fields=photo_100").text)

#with open("text.txt", "w") as outfile:
    #outfile.write("something")

with open("text.txt", "w") as outfile:
    outfile.write(requests.get("http://ya.ru").text)

#with open("text.txt", "r") as outfile:
    #print(outfile.read())