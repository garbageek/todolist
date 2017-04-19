from django.core.management.base import BaseCommand
from core.helpers import populate


class Command(BaseCommand):
    def handle(self, **options):
        populate()
