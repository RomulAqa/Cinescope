import pytest
import requests
from utils.data_generator import DataGenerator
from constants import BASE_URL, HEADERS, REGISTER_ENDPOINT, LOGIN_ENDPOINT

from pprint import pprint



@pytest.fixture(scope="session")
def test_user():
    email = DataGenerator.generate_random_email()
    random_name = DataGenerator.generate_random_name()
    random_pass = DataGenerator.generate_random_password()
    return {
        "email": email,
        "fullName": random_name,
        "password": random_pass,
        "passwordRepeat": random_pass,
        "roles": ["USER"]
    }



@pytest.fixture(scope="session")
def auth_session(test_user):
    # Регистрируем нового пользователя
    register_url = f"{BASE_URL}{REGISTER_ENDPOINT}"
    response = requests.post(
        register_url,
        json=test_user,
        headers=HEADERS
    )

    assert response.status_code == 201, "Ошибка регистрации пользователя"

    # Логинимся зарегистрированным пользователем
    login_url = f"{BASE_URL}{LOGIN_ENDPOINT}"

    login_data = {
        "email": test_user["email"],
        "password": test_user["password"]
    }

    response = requests.post(
        login_url,
        json=login_data,
        headers=HEADERS
    )

    assert response.status_code == 200, "Ошибка авторизации"

    # Получаем токен
    token = response.json().get("accessToken")
    assert token is not None, "Токен доступа отсутствует в ответе"

    # Создаём авторизованную сессию
    session = requests.Session()
    session.headers.update(HEADERS)
    session.headers.update({
        "Authorization": f"Bearer {token}"
    })

    return session