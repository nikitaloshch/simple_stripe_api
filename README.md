# Simple_Stripe_API
[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat-square&logo=Django)](https://www.djangoproject.com/)
[![docker](https://img.shields.io/badge/-Docker-464646?style=flat-square&logo=docker)](https://www.docker.com/)

Это веб-приложение на Django, интегрированное с API Stripe для обработки платежей.    

Приложение можно легко развернуть с использованием Docker.

## Стек
- Python
- Django
- Stripe
- python-dotenv


## Структура

- Модель Django: Item с полями (name, description, price, currency)
- API-точки:
  - `GET /buy/{id}`: Получение Stripe Session ID для оплаты определенного товара.
  - `GET /item/{id}`: Получение HTML-страницы с информацией о товаре и кнопкой "Купить".

## Установка с Docker

1. Клонировать и перейти в репозиторий:
   ```bash
   git clone https://github.com/nikitaloshch/simple_stripe_api.git
   cd simple_stripe_api
   cd backend
   ```

2. Создать файл `.env` в корне проекта и добавить следующее:
	 ```bash
	STRIPE_PUBLIC_KEY=YOUR_STRIPE_PUBLIC_KEY  
	STRIPE_SECRET_KEY=YOUR_STRIPE_SECRET_KEY  
	SECRET_KEY='SECRET_KEY' 
	```

3. Выполнить миграции:

	```bash
	docker-compose run web python manage.py makemigrations
	docker-compose run web python manage.py migrate
	```

4. Собрать докер образ:

	```bash
	docker-compose up --build
	```
5. Создать суперюзера:
	```bash
	python manage.py createsuperuser
	```
## Непосредственно использование 
Перейдите по адресу [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin), войдите в админку и добавьте товары.  

Перейдите на страницу товара, например, [http://127.0.0.1:8000/item/1/](http://127.0.0.1:8000/item/1/), чтобы увидеть информацию о товаре и кнопку "Купить".
	
