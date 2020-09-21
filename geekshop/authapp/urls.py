from django.urls import path

import geekshop.authapp.views as authapp

app_name = 'authapp'

urlpatterns = [
    re_path('login/', authapp.login, name='login'),
    re_path('logout/', authapp.logout, name='logout'),
    re_path('register/', authapp.register, name='register'),
    re_path('edit/', authapp.edit, name='edit'),

    re_path(r'^verify/(?P<email>,+)/(?P<activation_key>\w+)/$', authapp.verify, name='verify')
]
