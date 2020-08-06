python_dev_version = 3.6
python_prod_version = 3.5

DEV_VERSION = $(python_dev_version)
PROD_VERSION = $(python_prod_version)

all:
	python manage.py makemigrations --settings=django_architecture_design.settings.dev
	python manage.py migrate --settings=django_architecture_design.settings.dev
	python manage.py runserver 0.0.0.0:8889 --settings=django_architecture_design.settings.dev

dev:
	python manage.py runserver 0.0.0.0:8889 --settings=django_architecture_design.settings.dev

prod:
	python manage.py runserver 0.0.0.0:8889 --settings=django_architecture_design.settings.prod

test:
	python manage.py runserver 0.0.0.0:8889 --settings=django_architecture_design.settings.test
