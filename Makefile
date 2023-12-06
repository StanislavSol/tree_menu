install:
	poetry install

dev:
	poetry run python manage.py runserver

migrate:
	poetry run python manage.py makemigrations && poetry run python manage.py migrate
