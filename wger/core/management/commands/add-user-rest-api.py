from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from wger.core.models import ApiUser


class Command(BaseCommand):
    help = 'Command to create a new user via API'


    def add_arguments(self, parser):
        # add argurments/parameters to be used when creating a user
        parser.add_argument('username', type=str)
        parser.add_argument('email', type=str)
        parser.add_argument('password', type=str)
        parser.add_argument('created_by_username', type=str)

    def handle(self, *args, **options):
        # confirm created_by_username exists
        created_by = User.objects.filter(username=options["created_by_username"])
        if not created_by:
            raise CommandError(' {} is not registered user.'.format(options["created_by_username"]))

        if User.objects.filter(username=options["username"]):
            raise CommandError('Username {} already exists.'.format(options["username"]))

        if User.objects.filter(email=options["email"]):
            raise CommandError("Email {} already exists.".format(options["email"]))

        # if creator exists, username and email are not taken
        new_user = User.objects.create_user(username=options["username"],
                                            email=options["email"],
                                            password=options["password"])
        new_user.save()
        api_user = ApiUser(user=new_user, created_by=created_by[0])
        api_user.save()
        self.stdout.write("You have succesfully created an API user.")
