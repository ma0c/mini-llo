# Mini-llo

Mini-llo is a minimal version of [Trello](https://trello.com/), you can
register and create boards, it can be public or private.

On all boards once you're authenticated you can insert ideas. If you
have the board's ownership the idea will be published immediately, but
if not a request will be sent to the board's owner.

## Understanding the architecture

This is a simple django project, I like to structure all django applications
in a single folder called applications.

- [config](config) Has all the configurations, is the default folder
  create by the django-admin startproject
- [applications](applications) We put all applications in this folder
   applications are created by the django-admin startapp command
- [applicatinos/authentication](applications/authentication) All views
    and apis related to sign up and log in are in here
- [applicatinos/core](applications/core) All the code related to boards
    and ideas are in here

For each applications the following structure is used:
- api: Here we put all code related to web services, if we have more than
    one model, we transform api.py in a package that contains .py files
- context_processors.py: We store all context processor, a mechanism to
    inject variables in all templates without express it on get_context_data
- mixins.py: Some views require validations and the django way to manage
    is use a [Mixin pattern](https://en.wikipedia.org/wiki/Mixin) here we
    implement a segment of functionality to be extended
- templates: Standard django templates folder
- static: Standard django templates folder
- serializers.py: An elegant way implemented by [Django Rest Framework](https://www.django-rest-framework.org/)
    to transform REST request in models
- views: As the project grows, the views use to get bigger with time,
    so its better have an inner package for all views



To run it locally

```bash
python -m venv minillo_env
source minillo_env/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Build with docker

```bash
docker build -t ma0collazos/mini-llo .
docker run -p 8000:8000 ma0collazos/game-of-drones
```