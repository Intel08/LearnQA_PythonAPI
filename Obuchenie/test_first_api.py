import requests
import pytest

class TestFirstApi:
    names = [
        ("Maxim"),
        ("Dolya"),
        ("")
    ]

    @pytest.mark.parametrize('name', names)
    def test_hello_call(self, name):
        url = "https://playground.learnqa.ru/api/hello"
        data = {"name":name}

        responce = requests.get(url, params=data)

        assert responce.status_code == 200, "Wrong responce code"

        responce_dict = responce.json()
        assert "answer" in responce_dict, "There is no field 'answer' in the responce"

        if len(name) == 0:
            expected_responce_text = 'Hello, someone'
        else:
            expected_responce_text = f"Hello, {name}"

        actual_responce_text = responce_dict["answer"]
        assert actual_responce_text == expected_responce_text, "Actual text in the respomce is not correct"