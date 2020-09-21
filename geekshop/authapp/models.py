from django.db.models.functions import datetime
from django.utils.datetime_safe import datetime
from datetime import datetime
from datetime import timedelta

from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser

import pytz



class ShopUser(AbstractUser):
    SEX_MALE = 'male'
    SEX_FEMALE = 'female'
    SEX_CAT = 'cat'
    SEX_CHOICE = (
        {SEX_MALE: 'Мужской'},
        {SEX_FEMALE: 'Женский'},
        {SEX_CAT: 'Кот'}
    )
    avatar = models.ImageField(upload_to='users_avatars', blank=True)
    age = models.PositiveIntegerField(verbose_name = 'возраст', default=18)
    sex = models.CharField(max_length = 6, choices=SEX_CHOICE, default= SEX_CAT)

    activation_key = models.CharField(max_length=128, blank=True)
    activation_key_expires = models.DateTimeField(default = datetime.now() + datetime.timedelta(hours=12))

    def is_activation_key_expires(self):
        if datetime.now(pytz.timezone(settings.TIME_ZONE)) < self.activation_key_expires:
            return False
        else:
            return True

class ShopUserProfile(models.Model):
    user = models.OneToOneField(ShopUser, unique=True, null=False, db_index=True, on_delete=models.CASCADE)
    tagline = models.CharField(max_length=128, blank=True, verbose_name='тэги')
    aboutMe = models.TextField(blank=True, verbose_name='о себе')
    gender = models.CharField(choices=GENDER_CHOICES, max_length=1, blank=True, verbose_name='пол')

    @receiver(post_save, sender=ShopUser)
    def create_user_profile(self, sender, instance, created, **kwargs):
        if created:
            ShopUserProfile.object.create(user=instance)

    @receiver(post_save, sender=ShopUser)
    def save_user_profile(self, sender, instance, **kwargs):
        instance.shopuserprofile.save()
