from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from wger.core.models import ApiUser
from tabulate import tabulate


class Command(BaseCommand):

    def handle(self, **options):
        users = ApiUser.objects.all()
        all_users = []
        for user in users:
            all_users.append([user.user.username, user.user.email, user.created_by])
        print(tabulate(all_users, headers=["USERNAME", "EMAIL", "CREATED_BY"],
                       tablefmt="fancy_grid"))
