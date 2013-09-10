# encoding=utf-8
from django import forms
#from django.contrib.auth import get_user_model

from app1.models import MyUser


class MyForm(forms.ModelForm):
    date_of_birth = forms.CharField(label=u'生年月日')

    class Meta:
        model = MyUser


class SignupForm(forms.ModelForm):
    print('FFFFFFFFFFFFFFFFFFFFFFFFFF')
    date_of_birth = forms.CharField(label='birth date')

    class Meta:
        model = MyUser
        #model = get_user_model()

    def clean(self):
        print 'CLEAN'
        for x in self.cleaned_data:
            print x
        return self.cleaned_data


"""
from allauth.account.adapter import DefaultAccountAdapter


class MyAccountAdapter(DefaultAccountAdapter):
    print "MY ACCOUNT"

    def new_user(self, username=None, first_name=None, last_name=None,
                 email=None):
        print 'HOGEEEEEEEEEEEEEEEEEEEEEEEEEEE'

    def save_user(self, request, user, form, commit=True):
        print "SAVE USERRRRR"
        data = form.cleaned_data
        for d in data:
            print d
"""
