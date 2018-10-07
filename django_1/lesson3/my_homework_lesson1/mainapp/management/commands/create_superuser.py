from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Create superuser'

    def handle(self, *args, **options):
        
        User.objects.all().delete()
        super_user = User.objects.create_superuser('admin', 'django@test.com', 'xxXX1234')
        