# -*- coding: utf-8 -*-

from kay.utils.forms.modelform import ModelForm
from app.models import MyUser

class UserForm(ModelForm):
    class Meta:
        model = MyUser
        exclude = ('is_admin', 'activated', 'user_name', 'password')