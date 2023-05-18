from django.core.management.base import BaseCommand
from ihs_casualities.functions import login_to_website


class Command(BaseCommand):
    help = 'Checks the ihs'

    def handle(self, *args, **options):
        login_to_website()
        # self.stdout.write(self.style.SUCCESS('Successfully login'))

