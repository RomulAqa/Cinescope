import requests

BASE_URL = "https://restful-booker.herokuapp.com"

HEADERS = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}

booking_data = {
    "firstname": "Alex",
    "lastname": "Tester",
    "totalprice": 500,
    "depositpaid": True,
    "bookingdates": {
        "checkin": "2026-11-10",
        "checkout": "2026-11-15"
    },
    "additionalneeds": "Breakfast"
}

# Получает УРЛ
# Собирает нужный урл
# Отправляет запрос МЕТОД, ЕНДПОИНТ, Кварки
class CustomRequester: #
    def __init__(self, base_url):
        self.base_url = base_url


    def send_request(self, method, endpoint, **kwargs):
        full_url = f"{self.base_url}/{endpoint}"
        req_try = requests.request(method, full_url, **kwargs)
        return req_try


# req_for_class = CustomRequester(BASE_URL)
# try_send = req_for_class.send_request("GET", "booking/1")
#
# print(try_send.status_code)
# print(try_send.json())
# print("____")
#
# try_send_post = req_for_class.send_request("POST", "booking", json=booking_data, headers=HEADERS)
# assert try_send_post.status_code == 200
# try_send_post_json = try_send_post.json()
# assert try_send_post_json["booking"]["firstname"] == booking_data["firstname"]
















