import allure
import pytest
from jsonschema import validate
from data.schemas import POST_SCHEMA


@allure.title("Проверка получения списка всех постов")
def test_get_all_posts(post_service):
    response = post_service.get_posts()
    assert response.ok
    assert len(response.json()) == 100

@allure.title("Проверка содержимого конкретного поста (ID=1)")
def test_get_single_post(post_service):
    response = post_service.get_post_by_id(1)
    assert response.ok

    post_data = response.json()
    # Проверяем, что в ответе есть нужные ключи
    assert post_data["id"] == 1
    assert "title" in post_data
    print(f"\n Заголовок 1-го поста: {post_data['title'][:30]}...")

@allure.title("Создание нового поста")
def test_create_post(post_service):
    # Готовим данные для нового поста
    payload = {
        "title": "My new autotest",
        "body": "Some text of the new post",
        "userId": 1
    }
    # Отправляем POST-запрос. Данные передаем в параметре "data"  
    response = post_service.create_post(payload)
    # После создания нового объекта статус должен быть 201 (Created)
    assert response.status == 201
    # Проверяем, что сервер вернул нам созданный объект с новым ID
    result = response.json()
    assert result["title"] == payload["title"]
    assert "id" in result
    print(f"\n Создан пост с ID: {result['id']}")

@allure.title("Удаление существующего поста")
def test_delete_post(post_service):
    # Отправляем запрос на удаление поста с ID=1
    response = post_service.delete_post(1)
    assert response.status == 200, f"Ожидали 200, но получили {response.status}"
    # Проверяем, что нам вернулся пустой объект
    result = response.json()
    assert result == {}, f"Ожидали пустой объект, но получили {result}"
    print("\n Пост успешно удален")

@allure.title("Проверка схемы ответа")
def test_post_schema_validation(post_service):
    response = post_service.get_post_by_id(1)
    # Сверяем полученный JSON с чертежом POST_SCHEMA
    validate(instance=response.json(), schema=POST_SCHEMA)
    print("\n Схема ответа валидна!")

@allure.title("Негативные тесты для создания поста")
@pytest.mark.parametrize("invalid_payload, expected_status", [
    ({"title": 12345, "body": "text", "userId": 1}, 201), # Проверка, что можно записать числа вместо букв
    ({"body": "no title"}, 201),                          # Проверка на отсутствие обязательного поля
    ({}, 201)                                             # Пустой объект
])
def test_create_post_negative(post_service, invalid_payload, expected_status):
    response = post_service.create_post(invalid_payload)
    # В реальных проектах на плохие данные сервер должен отвечать статус кодом 400 (Bad Requests)
    assert response.status == expected_status
    print(f"\n Отправлено: {invalid_payload} | Статус: {response.status}")    

def test_create_post_with_faker(post_service, faker):
    # Генерация случайных данных
    payload = {
        "title": faker.sentence(),  # Случайное предложение
        "body": faker.paragraph(),  # Случайный абзац текста
        "userId": faker.random_int(min=1, max=10) # Случайное ID юзера от 1 до 10
    }

    response = post_service.create_post(payload)
    assert response.status == 201

    result = response.json()
    assert result["title"] == payload["title"]
    print(f"\n Сгенерированный заголовок: {payload["title"]}")


