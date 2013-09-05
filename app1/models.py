from django.contrib.auth.models import User
from django.db import models as m
from django.db.models.signals import post_save


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance, height=157.0)


post_save.connect(create_user_profile, sender=User)


class Profile(m.Model):
    user = m.OneToOneField(User)
    height = m.FloatField()


#class MyUser(AbstractBaseUser):
    #name = m.CharField()
    #height = m.FloatField()
    #USERNAME_FIELD = 'name'
