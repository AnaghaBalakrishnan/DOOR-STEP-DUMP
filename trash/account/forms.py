from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import *


class SignUpForm(UserCreationForm):
    # first_name=forms.CharField(max_length=30)
    # last_name=forms.CharField(max_length=30)
    # email=forms.EmailField()

    class Meta():
        model=User
        fields=['first_name','last_name','username','email','password1','password2']
        help_texts={
            'username' : None,
            'password1':None,
            'password2':None
        }



    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
       
        


        self.fields['password1'].help_text=None
        self.fields['password2'].help_text=None









class LogForm(forms.Form):
    username=forms.CharField(max_length=100,label='' , widget=forms.TextInput(attrs={'placeholder':'username','class':'input'}))
    password=forms.CharField(max_length=100,label='' , widget=forms.TextInput(attrs={'placeholder':'username','class':'input'}))


class ContactUsForm(forms.ModelForm):
    class Meta:
        model=ContactUs
        fields="__all__"