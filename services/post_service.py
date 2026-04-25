import allure

class PostService:
    def __init__(self, api_request_context):
        self.request = api_request_context

    @allure.step("Запрос всех постов")
    def get_posts(self):
        return self.request.get("/posts")

    @allure.step("Запрос поста по ID: {post_id}")
    def get_post_by_id(self, post_id):
        return self.request.get(f"/posts/{post_id}")

    @allure.step("Создание нового поста")
    def create_post(self, payload):
        return self.request.post("/posts", data=payload)

    @allure.step("Удаление поста по ID: {post_id}")
    def delete_post(self, post_id):
        return self.request.delete(f"/posts/{post_id}")