from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from authapp.models import ShopUser


class Command(BaseCommand):
    help = 'Create superuser'

    def handle(self, *args, **options):
        
        #User.objects.all().delete()
        #super_user = User.objects.create_superuser('admin', 'django@test.com', 'xxXX1234')
        super_user = ShopUser.objects.create_superuser('admin', 'django@geekshop.local', 'xxXX1234', age=33)
        