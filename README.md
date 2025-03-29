# Yatube API

REST API для социальной сети Yatube с функционалом публикации записей, подписки на авторов и комментирования.

## Основные возможности

- Аутентификация с использованием JWT
- Создание и редактирование публикаций
- Добавление комментариев к записям
- Подписка на других пользователей
- Группировка постов по сообществам
- Пагинация и поиск по записям

## Технологический стек

- Python 3.9+ 
- Django 3.2+
- Django REST Framework 3.12+
- SQLite 3

## Установка и запуск

1. Клонируйте репозиторий проекта:
```bash
git clone https://github.com/ваш-логин/api_final_yatube.git  
cd api_final_yatube 
```
2. Создайте и активируйте виртуальное окружение:
```bash
python -m venv venv  
source venv/bin/activate  # для Linux/MacOS  
venv\Scripts\activate  # для Windows  
```
3. Установите зависимости:
```bash
pip install -r requirements.txt  
```
4. Примените миграции:
```bash
python manage.py migrate  
```
5. Запустите сервер разработки:
```bash
python manage.py runserver
```

API будет доступно по адресу http://127.0.0.1:8000/