import allure

@allure.title("Проверка получения списка всех юзеров")
def test_get_all_users(users_service):
    response = users_service.get_users()
    assert response.ok
    assert len(response.json()) == 10

@allure.title("Проверка конкретного юзера на наличие информации")
def test_get_user_info(users_service):
    response = users_service.get_user_by_id(3)
    assert response.ok

    user_data = response.json()
    assert user_data["id"] == 3
    assert user_data["username"] == "Samantha"
    assert "email" in user_data
    assert "address" in user_data

@allure.title("Создание нового юзера")
def test_create_user(users_service):
    payload = {
        "name": "Ivan Ivanov",
        "username": "ivanov_ivan",
        "email": "ivanov@example.com",
        "address": {
            "street": "Lenina",
            "suite": "Apt. 555",
            "city": "Moscow",
            "zipcode": "12345-6789",
            "geo": {
                "lat": "-37.3159",
                "lng": "81.1496"
            }
        },
        "phone": "1-770-736-8031 x56442",
        "website": "ivanov.org",
        "company": {
            "name": "Ivanov-Group",
            "catchPhrase": "Multi-layered client-server neural-net",
            "bs": "harness real-time e-markets"
        }
    }
    response = users_service.create_user(payload)
    assert response.status == 201
    result = response.json()
    assert result["name"] == payload["name"]
    assert "email" in result
    print(f"\n Создан юзер с ID: {result['id']}")

@allure.title("Удаление существующего юзера")
def test_delete_user(users_service):
    response = users_service.delete_user(5)
    assert response.status == 200, f"Ожидали 200, но получили {response.status}"
    result = response.json()
    assert result == {}, f"Ожидали пустой объект, но получили {result}"
    print("\n Юзер успешно удален")
