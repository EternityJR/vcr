from django import forms
from .models import *


class CodeForm(forms.Form):
    source_file = forms.CharField(label="", widget=forms.Textarea(attrs={'cols': 100, 'rows': 12}))
