import pytest
from services.post_service import PostService
from services.users_service import UsersService
from faker import Faker

@pytest.fixture(scope="session")
def api_request_context(playwright):
    # Создаем один контекст на всю сессию тестов
    request_context = playwright.request.new_context(
        base_url="https://jsonplaceholder.typicode.com/"
        )
    yield request_context
    # Закрываем контекст после всех тестов
    request_context.dispose()

@pytest.fixture
def post_service(api_request_context):
    return PostService(api_request_context)

@pytest.fixture
def users_service(api_request_context):
    return UsersService(api_request_context)

@pytest.fixture(scope="session")
def faker():
    return Faker()