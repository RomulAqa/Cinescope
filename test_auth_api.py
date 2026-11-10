import pytest
import requests

#1. Создали данные пользователя
#2. Зарегистрировали пользователя
#3. Подготовили email + password
#4. Залогинились
#5. Получили accessToken
#6. Создали авторизованную Session

def test_positiv_auth(test_user, auth_session):
    req_post =