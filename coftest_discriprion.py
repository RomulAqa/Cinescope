# debug_auth.py
#
# Этот файл нужен ТОЛЬКО для того, чтобы увидеть глазами,
# что происходит внутри test_user + auth_session.
#
# Pytest здесь вообще не используется.

import requests
from pprint import pprint

from utils.data_generator import DataGenerator
from constants import BASE_URL, HEADERS, REGISTER_ENDPOINT, LOGIN_ENDPOINT


# ============================================================
# ШАГ 1. Делаем то, что обычно делает fixture test_user
# ============================================================

email = DataGenerator.generate_random_email()
random_name = DataGenerator.generate_random_name()
random_pass = DataGenerator.generate_random_password()

test_user = {
    "email": email,
    "fullName": random_name,
    "password": random_pass,
    "passwordRepeat": random_pass,
    "roles": ["USER"]
}

print("\n========== ШАГ 1. СОЗДАЛИ ДАННЫЕ ПОЛЬЗОВАТЕЛЯ ==========")
pprint(test_user)


# ============================================================
# ШАГ 2. Регистрируем пользователя
# Это первая часть fixture auth_session
# ============================================================

register_url = f"{BASE_URL}{REGISTER_ENDPOINT}"

print("\n========== ШАГ 2. РЕГИСТРАЦИЯ ==========")
print("URL:", register_url)
print("Отправляемые данные:")
pprint(test_user)

response = requests.post(
    register_url,
    json=test_user,
    headers=HEADERS
)

print("\nСтатус регистрации:", response.status_code)
print("Ответ сервера:")
pprint(response.json())

assert response.status_code == 201, "Ошибка регистрации пользователя"


# ============================================================
# ШАГ 3. Готовим данные для логина
# Берём email и password ТОГО ЖЕ пользователя
# ============================================================

login_url = f"{BASE_URL}{LOGIN_ENDPOINT}"

login_data = {
    "email": test_user["email"],
    "password": test_user["password"]
}

print("\n========== ШАГ 3. ДАННЫЕ ДЛЯ ЛОГИНА ==========")
print("URL:", login_url)
pprint(login_data)


# ============================================================
# ШАГ 4. Логинимся зарегистрированным пользователем
# ============================================================

response = requests.post(
    login_url,
    json=login_data,
    headers=HEADERS
)

print("\n========== ШАГ 4. ЛОГИН ==========")
print("Статус логина:", response.status_code)
print("Ответ сервера:")
pprint(response.json())

assert response.status_code == 200, "Ошибка авторизации"


# ============================================================
# ШАГ 5. Достаём accessToken из ответа на login
# ============================================================

token = response.json().get("accessToken")

print("\n========== ШАГ 5. ACCESS TOKEN ==========")
print(token)

assert token is not None, "Токен доступа отсутствует в ответе"


# ============================================================
# ШАГ 6. Создаём requests.Session()
# ============================================================

session = requests.Session()

# Добавляем обычные HEADERS
session.headers.update(HEADERS)

# Добавляем токен авторизации
session.headers.update({
    "Authorization": f"Bearer {token}"
})

print("\n========== ШАГ 6. SESSION ==========")
print("Session создана.")
print("Headers внутри Session:")
pprint(dict(session.headers))


# ============================================================
# ГОТОВО
# ============================================================

print("\n========== ВСЯ ЦЕПОЧКА ВЫПОЛНЕНА ==========")
print("1. Создали данные пользователя")
print("2. Зарегистрировали пользователя")
print("3. Подготовили email + password")
print("4. Залогинились")
print("5. Получили accessToken")
print("6. Создали авторизованную Session")