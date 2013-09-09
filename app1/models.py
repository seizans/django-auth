from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, User
from django.db import models as m


class MyUserManager(BaseUserManager):
    def create_user(self, email, date_of_birth, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, date_of_birth, password):
        user = self.create_user(
            email, password=password, date_of_birth=date_of_birth)
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    email = m.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
        db_index=True,
    )
    date_of_birth = m.DateField()
    is_active = m.BooleanField(default=True)
    is_admin = m.BooleanField(default=False)
    objects = MyUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['date_of_birth']

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def __unicode__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin


#class Profile(m.Model):
    #user = m.OneToOneField(User)
    #height = m.FloatField()


#class ProfileInline(admin.StackedInline):
    #model = Profile
    #can_delete = False
    #verbose_name_plural = 'profile'


#class UserAdmin(UserAdmin):
    #inlines = (ProfileInline,)


#admin.site.unregister(User)
#admin.site.register(User, UserAdmin)
