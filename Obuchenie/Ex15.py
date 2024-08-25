import requests
from lib.base_case import BaseCase
from lib.assertions import Assertions
class TestUserRegister(BaseCase):
    def test_create_user_successfully(self):
        data = self.prepare_registration_data()

        response = requests.post("https://playground.learnqa.ru/api/user/", data=data)

        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_has_key(response, "id")

    def test_create_user_with_existing_email(self):
        email = 'vinkotov@example.com'
        data = self.prepare_registration_data(email)

        responce = requests.post("https://playground.learnqa.ru/api/user/", data=data)

        Assertions.assert_code_status(responce, 400)
        assert responce.content.decode("utf-8") == f"Users with email '{email}' already exists", f"Unexpected responce content {responce.content}"

    def test_create_user_without_symbol(self):
        email = 'vinkotovexample.com'
        data = self.prepare_registration_data(email)

        responce = requests.post("https://playground.learnqa.ru/api/user/", data=data)

        Assertions.assert_code_status(responce, 400)
        assert responce.content.decode("utf-8") == f"Invalid email format", f"Unexpected responce content {responce.content}"

    def test_create_user_without_param(self):
        email = 'vinkotov@example.com'
        data = self.prepare_registration_data(email)
        del data['password']
        responce = requests.post("https://playground.learnqa.ru/api/user/", data=data)

        Assertions.assert_code_status(responce, 400)
        assert responce.content.decode("utf-8") == f"The following required params are missed: password", f"Unexpected responce content {responce.content}"

    def test_create_user_with_short_username(self):
        email = 'vinkotov@example.com'
        data = self.prepare_registration_data(email)
        data['username'] = data['username'][0]

        responce = requests.post("https://playground.learnqa.ru/api/user/", data=data)

        Assertions.assert_code_status(responce, 400)
        assert responce.content.decode("utf-8") == f"The value of 'username' field is too short", f"Unexpected responce content {responce.content}"

    def test_create_user_with_long_username(self):
        email = 'vinkotov@example.com'
        data = self.prepare_registration_data(email)
        data['username'] = "Данный параметр показывает количество слов, состоящих из букв различных алфавитов. Часто это буквы русского и английского языка, например, слово «стол», где «о» - буква английского алфавита. Некоторые копирайтеры заменяют в рдывлраывращышвраыщвращвшрзывшар"
        responce = requests.post("https://playground.learnqa.ru/api/user/", data=data)

        Assertions.assert_code_status(responce, 400)
        assert responce.content.decode("utf-8") == f"The value of 'username' field is too long", f"Unexpected responce content {responce.content}"

