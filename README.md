# Простой мессенджер на Django

Этот проект представляет собой простой мессенджер, построенный с использованием Django и Django REST framework. Проект обеспечивает базовый функционал мессенджера, такой как авторизация, отправка личных сообщений и настройка профиля пользователя.

## Установка

1. Клонируйте репозиторий:

```bash
git clone https://github.com/thetimkri/messenger_project/)https://github.com/thetimkri/messenger_project/

1. Установите зависимости:

pip install -r requirements.txt


Примените миграции:
bash
Copy code
python manage.py migrate
Создайте суперпользователя:
bash
Copy code
python manage.py createsuperuser
Запустите сервер:
bash
Copy code
python manage.py runserver
Использование
API Эндпоинты
api/token/ - получение токена аутентификации
api/token/refresh/ - обновление токена аутентификации
api/user-profile/ - обновление профиля пользователя
Авторизация
Для доступа к защищенным эндпоинтам, необходимо предоставить токен аутентификации. Получите токен, отправив POST-запрос на /api/token/ с вашими учетными данными. Используйте полученный токен в заголовке "Authorization" при отправке запросов.
