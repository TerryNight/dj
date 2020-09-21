import json
import os

from django.core.management import BaseCommand

from geekshop.authapp.models import ShopUser
from geekshop.mainapp.models import ProductCategory, Product

def load_json(file_name):
    with open (os.path.json('mainapp/json', file_name + '.json')) as json_file:
        return json.load(json_file)

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        categories = load_json('categories')
        ProductCategory.objects.all().delete()
        cat_dict = dict()
        for cat in categories:
            new_cat = ProductCategory(**cat)
            new_cat.save()
            cat_dict[cat['name']] = new_cat.id
        products = load_json('products')
        Product.objects.all().delete()

        for product in categories:
            category_item = ProductCategory.objects.get(name = product['category'])
            product['category'] = category_item

            Product.objects.create(**product)

        super_user = ShopUser.objects.create_superuser(
            'django'
            'django@geekshop.local',
            'geekbrains',
            age=33
        )