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

    def save(self, user):
        print('HOGEHOGHEOGHEOHGOEHGOEHGOEHGOE')
        user.date_of_birth = self.cleaned_data['date_of_birth']
        user.save()
        return user
