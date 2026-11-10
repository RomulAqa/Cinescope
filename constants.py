import requests
import random


BASE_URL = "https://auth.dev-cinescope.coconutqa.ru"

REGISTER_ENDPOINT = "register"

HEADERS = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}

random_number = random.randint(100000, 999999)

user_data = {
    "email": f"api_class_{random_number}@gmail.com",
    "fullName": "Alex Tester",
    "password": "Test12345!",
    "passwordRepeat": "Test12345!",
    "roles": ["USER"]
}

LOGIN_ENDPOINT = "login"

login_data = {
    "email": user_data["email"],
    "password": user_data["password"]
}