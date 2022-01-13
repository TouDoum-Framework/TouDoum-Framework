from os import environ
from string import ascii_letters
from random import choice

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError
from  django.db.utils import IntegrityError
from rest_framework.authtoken.models import Token


class Command(BaseCommand):
    help = 'Register token list to db'

    def add_arguments(self, parser):
        parser.add_argument('--username', type=str)
        parser.add_argument('--password', type=str)
        parser.add_argument('--token', type=str)

    def handle(self, *args, **options):
        username = environ.get("TOKEN_USER_NAME", "tokener")
        password = environ.get("TOKEN_USER_PASS", ''.join(choice(ascii_letters) for _ in range(10)))
        key = environ.get("TOKEN_USER_CONTENT")

        if options["username"] is not None:
            username = options["username"]

        if options["password"] is not None:
            password = options["password"]

        if options["token"] is not None:
            key = options["token"]

        user = None
        try:
            user = User.objects.get(username=username)
            self.stdout.write(self.style.SUCCESS("Create User Token |> User Found !"))
        except User.DoesNotExist:
            self.stdout.write(self.style.ERROR("Create User Token |> User not found creating it !"))

            User.objects.create_user(
                username=username,
                password=password
            )
            self.stdout.write(self.style.SUCCESS("Create User Token |> User created"))
            self.stdout.write(self.style.SUCCESS("Create User Token |> Password %s" % password))

        try:
            Token.objects.get(user=user)
            self.stdout.write(self.style.SUCCESS("Create User Token |> Token for this user early exist"))
        except Token.DoesNotExist:
            try:
                if key is not None:
                    token = Token.objects.create(user=user, key=key)
                else:
                    token = Token.objects.create(user=user)
                self.stdout.write(self.style.SUCCESS("Create User Token |> Token created '%s'" % token.key))
            except IntegrityError:
                raise CommandError("Create User Token |> Token early exist nearby on db for other user please use "
                                   "other token")
