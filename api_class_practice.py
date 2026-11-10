import requests
import random
from constants import (
    BASE_URL,
    REGISTER_ENDPOINT,
    LOGIN_ENDPOINT,
    HEADERS,
    user_data,
    login_data
)

from mini_requester import CustomRequester




class AuthAPI(CustomRequester):

    def register_user(self, user_data):
        # full_url = f"{self.base_url}/{REGISTER_ENDPOINT}"
        # req_post = requests.post(full_url, json=user_data, headers=HEADERS)
        req_reqgister = self.send_request("POST", REGISTER_ENDPOINT, json=user_data, headers=HEADERS)
        return req_reqgister

    def login_user(self, some_data):
        # full_url_log = f"{self.base_url}/{LOGIN_ENDPOINT}"
        # req_post = requests.post(full_url_log, json=some_data,  headers=HEADERS)
        req_login = self.send_request("POST", LOGIN_ENDPOINT, json=some_data, headers=HEADERS)
        return req_login


try_class = AuthAPI(BASE_URL)

try_reg =  try_class.register_user(user_data)

print(try_reg.status_code)
print(try_reg.text)

try_login = try_class.login_user(login_data)
print(try_login.status_code)
print(try_login.text)

