import allure


@allure.title("Интеграционный тест: Пост -> Автор")
def test_post_has_valid_user(post_service, users_service):
    # Получаем пост через сервис постов
    post_responce = post_service.get_post_by_id(1)
    post_data = post_responce.json()
    user_id = post_data["userId"]
    # Используем полученный ID, чтобы запросить автора через сервис пользователей
    user_responce = users_service.get_user_by_id(user_id)
    # Проверяем, что автор существует
    assert user_responce.status == 200
    user_data = user_responce.json()
    print(f"\n Пост написал пользователь: {user_data['name']}")