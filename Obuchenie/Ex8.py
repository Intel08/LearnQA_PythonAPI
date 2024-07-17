import requests, time, json

responce = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job")

status1 = '{"status":"Job is NOT ready"}'
status2 = "Job is ready"
a = json.loads(responce.text)
token = (a['token'])
b = (a['seconds'])
print(token)
print(b)

responce2 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params= {"token": token})
c = responce2.text
print(c)
if c == status1:
    time.sleep(b)
    d = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={"token": token})
    d1 = d.text
    d2 = json.loads(d1)
    print(d2)
    result = (d2['result'])
    stat = (d2['status'])
    print(result)
    print(stat)
    if stat == status2 and result is not None:
        print("Результат есть")
    else:
        print("Результата нет")
else:
    print("Error")


