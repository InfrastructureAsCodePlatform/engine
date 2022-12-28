from os import environ

from django.core.management.base import BaseCommand

from harakiri.users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        if environ.get("SYSTEM_EMAIL") and environ.get("SYSTEM_PASSWORD"):
            if not User.objects.filter(email=environ["SYSTEM_EMAIL"]).exists():
                User.objects.create_superuser(environ["SYSTEM_EMAIL"], environ["SYSTEM_PASSWORD"])
