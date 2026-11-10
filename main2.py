import pytest

user_id = 777

@pytest.fixture
def create_user():
    print("Создаём пользователя")
    yield user_id
    print("Удаляем пользователя")


def test_user_id(create_user):
    print("Выполняется тест")
    assert create_user == 777

print("Проверка работы Git-ветки")