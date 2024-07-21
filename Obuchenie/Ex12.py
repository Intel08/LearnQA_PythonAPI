import requests

response = requests.get("https://playground.learnqa.ru/api/homework_header")
print(response.headers.get("x-secret-homework-header"))
assert response.headers.get("x-secret-homework-header") == "Some secret value", f"Значение cookie верное"