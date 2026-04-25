# Playwright API Automation Project ({JSON} Placeholder)

Это учебный проект по автоматизации тестирования API-интерфейса сайта [{JSON} Placeholder](https://jsonplaceholder.typicode.com/).

## Стек технологий
* **Python** 
* **Playwright APIRequestsContext** (библиотека для сетевых запросов)
* **Pytest** (тест-раннер)
* **API Client / Service Layer** (архитектура разделения логики)
* **JSON Schema** (валидация структуры ответов)

## Реализованные проверки
- [x] **CRUD операции**: GET (списки и конкретные объекты), POST (создание), DELETE (удаление).
- [x] **Интеграционные тесты**: Проверка связи между сущностями (Post -> User).
- [x] **Валидация схем**: Проверка соответствия ответов сервера ожидаемому формату JSON.
- [x] **Reporting**: Настроена генерация отчетов Allure.


## Как запустить проект

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/
   cd playwright_api_practice

2. Создайте и активируйте виртуальное окружение:
    ```bash
    python -m venv venv
    source venv/bin/activate  # Для Mac/Linux
    .\venv\Scripts\activate   # Для Windows

3. Установите зависимости:
    ```bash
    pip install -r requirements.txt
    playwright install

4. Запустите тесты:
    ```bash
    pytest -v -s --alluredir=allure-results