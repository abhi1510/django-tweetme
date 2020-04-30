# django-tweetme
A twitter like application created using Django 

### Instructions:

Create migrations

```
python manage.py makemigrations
python manage.py migrate
```

Create and load fixtures

```
python ../fixtures-creator.py
python manage.py loaddata users/fixtures/users.json
python manage.py loaddata users/fixtures/users.json
python manage.py loaddata tweets/fixtures/tweets.json
```

Finally runserver

```
python manage.py runserver
```
