from json.decoder import JSONDecodeError
import requests

responce = requests.get("https://playground.learnqa.ru/api/get_text")
print(responce.text)

try:
    parsed_responce_text = responce.json()
    print(parsed_responce.json)
except JSONDecodeError:
    print("Responce in not JSON format")
