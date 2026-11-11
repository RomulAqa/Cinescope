import requests

BASE_URL = "https://api.dev-cinescope.coconutqa.ru"

params = {
    "pageSize": 10,
    "page": 1,
    "minPrice": 100,
    "maxPrice": 1000,
    "locations": ["MSK", "SPB"],
    "published": True,
    "genreId": 1,
    "createdAt": "asc"
}

# ЗАДАНИЕ:
# 1. Отправь GET-запрос на /movies с параметрами params.
#
# 2. Проверь, что статус ответа 200.
#
# 3. Преобразуй ответ в JSON.
#
# 4. Проверь наличие обязательных полей:
#    movies, count, page, pageSize, pageCount.
#
# 5. Проверь типы:
#    movies — list
#    count — int
#    page — int
#    pageSize — int
#    pageCount — int
#
# 6. Проверь, что page == 1 и pageSize == 10.



















