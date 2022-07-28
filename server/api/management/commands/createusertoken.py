from os import environ
from string import ascii_letters
from random import choice

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError
from django.db.utils import IntegrityError
from dotenv import load_dotenv
from rest_framework.authtoken.models import Token


def random_pass(letter: int):
    return ''.join(choice(ascii_letters) for _ in range(letter))


class Command(BaseCommand):
    help = 'Register token list to db'

    def add_arguments(self, parser):
        parser.add_argument('--username', type=str)
        parser.add_argument('--password', type=str)
        parser.add_argument('--token', type=str)
        parser.add_argument('--use-env-var', action='store_true')

    def handle(self, *args, **options):

        username, password, key = None, None, None

        if options["use_env_var"]:
            load_dotenv(".env")
            username = environ.get("TOKEN_USER_NAME", "tokener")
            password = environ.get("TOKEN_USER_PASS", random_pass(10))
            key = environ.get("TOKEN_USER_CONTENT")

        if options["username"] is not None:
            username = options["username"]

        if options["password"] is not None:
            password = options["password"]

        if password is not None:
            password = random_pass(10)

        if options["token"] is not None:
            key = options["token"]

        if username is None or password is None:
            raise CommandError("Create User Token |> Please et user and password")

        try:
            user = User.objects.get(username=username)
            self.stdout.write(self.style.SUCCESS("Create User Token |> User %s Found !" % user.username))
        except User.DoesNotExist:
            self.stdout.write(self.style.ERROR("Create User Token |> User not found creating it !"))

            user = User.objects.create_user(
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
