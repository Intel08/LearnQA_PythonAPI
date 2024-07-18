import requests

response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type")
print(response.text)

payload = {"method": "GET"}
response = requests.head("https://playground.learnqa.ru/ajax/api/compare_query_type", params=payload)
print(response.text)

payload = {"method": "PUT"}
response = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", data=payload)
print(response.text)