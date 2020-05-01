from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

from fixtures_creator import fetch_users

class Command(BaseCommand):
    help = 'Create initial users'

    def handle(self, *args, **kwargs):
        _status, _json = fetch_users()
        if _status == 200:

            User.objects.create_superuser(username='admin', email='admin@example.com', 
                    first_name='admin', password='admin@123')

            for u_data in _json:
                fname, lname = u_data.get('name').split(' ')[:2]
                username = u_data.get('username')
                email = u_data.get('email')
                user = User.objects.create_user(username=username, email=email, first_name=fname,
                    last_name=lname, password='password')

                address = u_data.get('address', {})
                user.profile.location = address.get('suite') + ',' + address.get('city')
                user.profile.bio = u_data.get('company', {}).get('bs')
                user.save()
                print(f'Added user with id: {user.id}')
        else:
            raise Exception('Error fetching users!')