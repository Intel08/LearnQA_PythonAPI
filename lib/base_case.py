import json.decoder

from requests import Response
class BaseCase:
    def get_cookie (self, responce: Response, cookie_name):
        assert cookie_name in responce.cookies, f"Cannot find cookie with name {cookie_name} in the last responce"
        return responce.cookies[cookie_name]

    def get_header (self, responce: Response, headers_name):
        assert headers_name in responce.headers, f"Cannot find header with the name {headers_name} in tje last responce"
        return responce.headers[headers_name]

    def get_json_value(self, responce: Response, name):
        try:
            responce_as_dict = responce.json()
        except json.decoder.JSONDecodeError:
            assert False, f"Responce is not in JSON format/ Responce text is {responce.text}"

        assert name in responce_as_dict, f"Responce JSON doesn't have key {name}"

        return responce_as_dict[name]
