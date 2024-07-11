import requests

headers = {"some_header": "123"}
responce = requests.get("https://playground.learnqa.ru/api/show_all_headers", headers = headers)

print(responce.text)
print(responce.headers)