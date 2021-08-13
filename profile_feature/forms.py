from django import forms
from .models import OnePost
import datetime
from django import forms
from django.contrib.auth.models import User
from .models import Account

class changeBioForm(forms.Form):
    error_messages = {
        'required': 'Please type',
    }
    pos_attrs = {
        'type': 'text',
        'class': 'todo-form-input',
        'placeholder':'Your status'
    }
    title_attrs = {
        'type': 'text',
        'class': 'todo-form-input',
        'placeholder':'Your Post'
    }

    Status = forms.CharField(label='', required=True, max_length=40, widget=forms.Textarea(attrs=pos_attrs))
