# django-tweetme
A twitter like application created using Django 

### Instructions:

Create migrations and dump users

```
python manage.py makemigrations
python manage.py migrate
python manage.py dump_users
python manage.py createsuperuser
```

Create and load fixtures

```
python fixtures-creator.py
python manage.py loaddata tweets/fixtures/tweets.json
```

Finally runserver

```
python manage.py runserver
```
