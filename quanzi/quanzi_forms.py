# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 15:01:38 2015

@author: jin
"""
from django import forms


class RegisterForm(forms.Form):
    user_email = forms.EmailField(label='email')
    user_name = forms.CharField(label='name', max_length=20)
    user_pw = forms.CharField(label='password', max_length=30)
    user_birthday = forms.DateField(label='birthday', required=False)
    user_school = forms.CharField(label='school', max_length=20)
    user_gender = forms.BooleanField(label='gender', required=False)
    
