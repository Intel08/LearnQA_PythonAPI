import requests

responce = requests.get("https://playground.learnqa.ru/api/long_redirect", allow_redirects=True)
first_responce = responce.history[0]
second_response = responce.history[1]
third_responce = responce

print(first_responce.url)
print(second_response.url)
print(third_responce.url)