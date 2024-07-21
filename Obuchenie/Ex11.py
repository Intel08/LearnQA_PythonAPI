import requests

response = requests.get("https://playground.learnqa.ru/api/homework_cookie")
print(response.cookies.get("HomeWork"))
assert response.cookies.get("HomeWork") == "hw_value", f"Значение cookie верное"
