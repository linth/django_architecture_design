# Django_architecture_design
This is a side-project for general stuff/structure whatever creating a new project.

# Getting Started
## :one: clone the project.
```
$ git clone https://github.com/linth/django_architecture_design.git
```

## :two: install packages/modules what you need.
```
$ pip install -r requirement.txt

$ pip install -r requirements.requirement_dev.txt # for dev.
$ pip install -r requirements.requirement_test.txt # for test.
$ pip install -r requirements.requirement_prod.txt # for prod.
```

## :three: run your application.
```
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver # for genereal case.

$ python manage.py runserver --settings=django_architecture_design.settings.dev # for dev.
$ python manage.py runserver --settings=django_architecture_design.settings.test # for test.
$ python manage.py runserver --settings=django_architecture_design.settings.prod # for prod.
```

## :four: open browser to watch your page.
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
- [ ] multiple database (dev, test, prod)
- [ ] logging
- [ ] swagger
- [ ] WSGI and ASGI
- [ ] Cross-Origin Resource Sharing (CORS)
- [ ] django rest framework (CRUD)
- [ ] django function-based view (CRUD)
- [ ] django class-based view (CRUD)
- [ ] User authentication (customer)
- [ ] auth and permission (for default)
- [ ] auth and permission ([django-allauth](https://django-allauth.readthedocs.io/en/latest/index.html))
- [ ] shell script (several command-lines for doing something.)
- [ ] 400/403/404/500 page

#

# Reference
