from django.urls import path

import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
path('', mainapp.products, name='products'),
path('all', mainapp.products, name='products_all'),
path('home', mainapp.products, name='products_home'),
path('office', mainapp.products, name='products_office'),
path('modern', mainapp.products, name='products_modern'),
path('classic', mainapp.products, name='products_classic'),
]