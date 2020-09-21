from django.core.management.base import BaseCommand
from mainapp.models import ProductCategory, Product
from authapp.models import ShopUser

import json, os

from geekshop.authapp.models import ShopUserProfile


class Command(BaseCommand):


    def handle(self, *args, **options):
        users = ShopUser.objects.all()
        for user in users:
            user_profile = ShopUserProfile.objects.create()
            user_profile.save()

