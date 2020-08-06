<<<<<<< HEAD
# django_architecture_design
This is a side-project for general stuff/structure whatever creating a new project.

=======
# Django_architecture_design
This is a side-project for general stuff/structure whatever creating a new project.
>>>>>>> e529b3c6abe7feb9855854a3345b72bbc24a3bde

# Getting Started
:one: clone the project.
```
$ git clone https://github.com/linth/django_architecture_design.git
```

:two: install packages/modules what you need.
```
$ pip install -r requirement.txt

$ pip install -r requirements.requirement_dev.txt # for dev.
$ pip install -r requirements.requirement_test.txt # for test.
$ pip install -r requirements.requirement_prod.txt # for prod.
```

:three: run your application.
```
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver # for genereal case.

$ python manage.py runserver --settings=django_architecture_design.settings.dev # for dev.
$ python manage.py runserver --settings=django_architecture_design.settings.test # for test.
$ python manage.py runserver --settings=django_architecture_design.settings.prod # for prod.
```

:four: open browser to watch your page.
```
http://localhost:8000/app/
```

## :five: use [Google](https://www.google.com/), [Django](https://www.djangoproject.com/), [stackoverflow](https://stackoverflow.com/) to solve your issues.

---
# Django structure
- [x] django project
- [x] django application (app, app2, app3, ..., etc)
- [x] django api
- [x] settings (dev, test, prod)
- [x] templates
- [x] static
- [x] bootstrap
- [x] requirement.txt (dev, test, prod)
- [ ] multiple database for dev, test, prod (MySQL, MSSQL, PostgreSQL, NoSQL)
- [ ] environment for dev, test, prod (virtualenv, pipenv)
- [ ] docker and kubernetes
- [ ] core
- [ ] logging
- [ ] swagger ([Django REST Swagger](https://django-rest-swagger.readthedocs.io/en/latest/))
- [ ] WSGI and ASGI
- [x] Cross-Origin Resource Sharing (CORS)
- [ ] django rest framework (CRUD)
- [ ] django function-based view (CRUD)
- [ ] django class-based view (CRUD)
- [ ] User authentication ([Allauth](https://django-allauth.readthedocs.io/en/latest/))
- [ ] User authentication (customer)
- [ ] auth and permission (for default)
- [ ] auth and permission ([django-allauth](https://django-allauth.readthedocs.io/en/latest/index.html))
- [ ] shell script (several command-lines for doing something.)
- [ ] CI/CD
- [ ] django unit testing
- [ ] [django debug toolbar](https://django-debug-toolbar.readthedocs.io/en/latest/)
- [ ] crontab or celery for schedule
- [ ] websocket
- [ ] webhook
- [ ] AJAX (axios, ajax)
- [ ] JWT
- [x] Makefile
- [ ] 400/403/404/500 page

# Author
linth

# Reference
- https://sunscrapers.com/blog/10-django-packages-you-should-know/
