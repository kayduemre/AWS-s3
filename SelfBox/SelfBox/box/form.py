from django import forms

class Fileform(forms.Form):

    select = forms.CharField(label='select', max_length=100)
    