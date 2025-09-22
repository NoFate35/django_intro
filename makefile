server:
	poetry run manage.py runserver

test:
	poetry run python3 manage.py test tests/
