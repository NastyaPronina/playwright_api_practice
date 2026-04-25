import allure


class UsersService:
    def __init__(self, api_request_context):
        self.request = api_request_context

    @allure.step("Запрос всех юзеров")
    def get_users(self):
        return self.request.get("/users")

    @allure.step("Запрос юзера по ID: {user_id}")
    def get_user_by_id(self, user_id):
        return self.request.get(f"/users/{user_id}")

    @allure.step("Создание нового юзера")
    def create_user(self, payload):
        return self.request.post("/users", data=payload)

    @allure.step("Удаление юзера по ID: {user_id}")
    def delete_user(self, user_id):
        return self.request.delete(f"/users/{user_id}")
