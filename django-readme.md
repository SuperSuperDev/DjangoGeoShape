# Seeding Data in Django

## django -

- Have Django create a seeds file automatically from the data that already exists in the table `python manage.py dumpdata app-name --output app-name/seeds.json --indent=2` - Depending on if you need to change this data at all, or add more, this command could be a one time thing.
- Empty the database of all rows inside currently. `python manage.py flush` and answer "yes" when prompted.
- Load your data from the seeds file, back into the database. `python manage.py loaddata app_name/seeds.json`
- Create your superuser again, as you have been deleted too `python manage.py createsuperuser`

## Resetting a Postgres DB w/Django

## django

- Drop the database `dropdb db_name`
- Delete migration...except `__init__.py`
- create the db again, `createdb db_name`
- make migration `python manage.py makemigrations`
- migrate `python manage.py migrate`
- If you want to re seed, you can now `python loadata .......`

## Setting up a Django Project - DRF

## Django

- Create a new environment, and install Django into it `pipenv install django`
- ✅Enter into that virtual environment with the command `pipenv shell`. You should see the command prompt change slightly
- ✅Start a new Django Project `django-admin startproject project .`
- ✅If not prompted by VS Code, install pylint `pipenv install pylint`. Create a `.pylintrc` file in the root of your project and add the following rules

```.pylint
[MESSAGES CONTROL]
disable=arguments-differ,missing-function-docstring,missing-class-docstring,no-self-use,raise-missing-from,no-member,missing-module-docstring,invalid-name,too-few-public-methods, relative-beyond-top-level
```

- Hook up Postgres as the database. (Skip if using SQL Lite)
  - ✅ Navigate to `project/settings.py` and find the dictionary called `DATABASES`
  - ✅ Replace Database section with

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'jurrasic-django-db',
        'HOST': 'localhost',
        'PORT': 5432
    }
}
```

## Install database adapter for Django/Postgres  

```pipenv install psycopg2-binary```
    *   ✅ Create the database in Postgres `createdb name-of-database`

- ✅ Run the initial migrations for the app, to create all the default tables `python manage.py migrate`
- ✅ Start the App `python manage.py runserver`
- ✅ Visit the landing page at `localhost:8000` to check all is running successfully
- ✅ Create a super user for the admin app, `python manage.py createsuperuser` answer prompts using sensible defaults
- ✅ Navigate to the admin site at `localhost:8000/admin` and login in with your super user credentials

## Creating Django Apps

- Create a new app within the project `django-admin startapp app-name`
- Register my new app in the `project/settings.py`
- Create my model for my new resource in the `app-name/models.py`
- Have Django check that new model and prepare to create the table for it in the database `python manage.py makemigrations`
- If all is fine, have it actually run those changes `python manage.py migrate`
- Register your app with the admin site in `app-name/admin.py`
  - Run your server and visit the admin app `localhost:8000/admin`
  - Add a `__str__` method to your class to make your items easier to read in the admin app.

## Install Django and create Environment

### Create a new environment, and install Django into it

`pipenv install django`

- Enter into that virtual environment with the command `pipenv shell`. You should see the command prompt change slightly
- Start a new Django Project `django-admin startproject project .`
- If not prompted by VS Code, install pylint for this project `pipenv install pylint` + create `.pylintrc`
- Run the initial migrations for the app, to create all the default tables `python manage.py migrate`
- Start the App `python manage.py runserver`
- Visit the landing page at `localhost:8000` to check all is running successfully
- Create a super user for the admin app, `python manage.py createsuperuser` answer prompts using sensible defaults
- Navigate to the admin site at `localhost:8000/admin` and login in with your super user credentials

## Custom User Django

### django Start New App

- Start a new app, for my custom user. `django-admin startapp jwt_auth`
- Add that new app to your `project/settings.py INSTALLED_APPS`
- Let Django know, to use the model we are now going to create. Add to `project/settings.py` , `AUTH_USER_MODEL = jwt_auth.User'`
- Go and create our new User model. Alter or add any new fields to the User model.
- Make and Migrate that new model.
- You may now need to reset your DB
- Add your new user model to the admin site.

### Token Auth - Django

- Add the Python Json Web Token package. `pipenv install pyjwt`
- Create a `jwt_auth/authentication.py` file, this will play the same role as `secureRoute` and will prevent non logged in requests working.
- Add my custom authentication settings to the `project/settings.py`

```python
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'jwt_auth.authentication.JWTAuthentication'
    ],
}
```

- Add a user serializer serializer at `jwt_auth/serializers/common.py`
- Add Register and Login view controllers at `jwt_auth/views.py`
- Add `jwt_auth/urls.py` file, and hook up to project urls.
- Add permission classes to any views you now want to be protected by authentication.

### JWT Model(?) Django

```python
from rest_framework.authentication import BasicAuthentication
from rest_framework.exceptions import PermissionDenied
from django.contrib.auth import get_user_model
from django.conf import settings
import jwt
User = get_user_model()
class JWTAuthentication(BasicAuthentication):
    def authenticate(self, request):
        header = request.headers.get('Authorization')
        if not header:
            return None
        if not header.startsWith('Bearer'):
            raise PermissionDenied({'detail': 'Invalid Authorization Header'})
        token = header.replace('Bearer ', '')
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
            user = User.objects.get(pk=payload.get('sub'))
        except jwt.exceptions.InvalidTokenError:
            raise PermissionDenied({'detail': 'Invalid Token'})
        except User.DoesNotExist:
            raise PermissionDenied({'detail': 'User Not Found'})
        return (user, token)
```
