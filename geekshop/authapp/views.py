from django.core.mail import send_mail
from django.db import transaction
from django.shortcuts import render, HttpResponseRedirect
from geekshop.authapp.forms import ShopUserLoginForm, ShopUserRegisterForm
from django.contrib import auth
from django.urls import reverse

from geekshop.authapp.forms import ShopUserEditForm
from geekshop.authapp.models import ShopUser
from geekshop.geekshop import settings


def send_verify_email(user):
    verify_link = reverse('auth:veryify', args = [user.email,user.activation_key])
    title = 'Подтверждение почты пользователя' + user.username

    message = f'{settings.DOMAIN_NAME}{verify_link}'

    return send_mail(title, message, settings.EMAIL_HOST_USER, [user.email], fail_silently=True)

def verify(request, email, activation_key):
    try:
        user = ShopUser.objects.get(email=email)
        if user.activation_key == activation_key and not user.is_activation_key_expired():
            user.is_active = True
            user.save()
            auth.login(request, user)
            return render(request, 'authapp/verification.html')
        else:
            return render (request, 'authapp/verification.html')
    except Exception as ex:
        print(ex)
        return HttpResponseRedirect(reverse('main'))

def login(request):
    title = 'вход'
    
    login_form = ShopUserLoginForm(data=request.POST or None)  
    if request.method == 'POST' and login_form.is_valid():
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect(reverse('main'))

    content = {'title': title, 'login_form': login_form}
    return render(request, 'authapp/login.html', content)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main'))
    

def register(request):
    title = 'регистрация'
    
    if request.method == 'POST':
        register_form = ShopUserRegisterForm(request.POST, request.FILES)
    
        if register_form.is_valid():
            register_form.save()
            send_verify_email(user)
            return HttpResponseRedirect(reverse('auth:login'))
    else:
        register_form = ShopUserRegisterForm()
    
    content = {'title': title, 'register_form': register_form}
    
    return render(request, 'authapp/register.html', content)
    
    
@transaction.atomic
def edit(request):
    title = 'редактирование'
    
    if request.method == 'POST':
        edit_form = ShopUserEditForm(request.POST, request.FILES, instance=request.user)
        profile_form = ShopUserEditForm(request.POST, instance=request.user.shopuserpeofile)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('auth:edit'))
    else:
        edit_form = ShopUserEditForm(instance=request.user)
        profile_form = ShopUserEditForm(instance=request.user.shopuserpeofile)
    
    content = {'title': title, 'edit_form': edit_form, 'profile_form': profile_form}
    
    return render(request, 'authapp/edit.html', content)