# -*- coding: utf-8 -*-
# author: #_# <jccjd> ^_^

from django import forms
class NameForm(forms.Form):
    your_name = forms.CharField(label='You name', max_length=100)



