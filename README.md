# django-tweetme
A twitter like application created using Django 

### Highlights:

* Tweet - CRUD
* Followers and Following
* Search for any user
* Notifications using SSE on post liked.


### Instructions:

Create migrations and dump users

```
python manage.py makemigrations
python manage.py migrate
python manage.py dump_users
```

Create and load fixtures

```
python fixtures_creator.py
python manage.py loaddata tweets/fixtures/tweets.json
```

Finally runserver

```
python manage.py runserver
```
