from django import forms

class QuestionForm(forms.Form):
    things = forms.CharField(label='things', max_length=200, widget=forms.TextInput())
    location = ""