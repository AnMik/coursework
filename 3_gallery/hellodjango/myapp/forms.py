# -*- coding: utf-8 -*-
from django import forms


class MyImageForm(forms.Form):
    image = forms.ImageField()
