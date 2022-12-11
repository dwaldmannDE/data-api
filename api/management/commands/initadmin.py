import os
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        username = os.environ.get('DJANGO_SU_NAME', 'admin')
        email = os.environ.get('DJANGO_SU_EMAIL', 'admin@example.org')
        password = os.environ.get('DJANGO_SU_PASSWORD', 'password')

        if not User.objects.filter(username=username).exists():
            print('Creating account for %s (%s)' % (username, email))
            admin = User.objects.create_superuser(
                email=email, username=username, password=password)
        else:
            print('Admin account has already been initialized.')
