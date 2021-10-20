from typing import Text
from django import forms

class PostForm(forms.Form):
    title = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Enter title of entry'}))
    text = forms.CharField(required=True, widget=forms.Textarea(attrs={'placeholder': 'Enter markdown text here'}))

class EditForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea(), label='')