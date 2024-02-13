from django import forms


class tamas(forms.Form):
    name = forms.CharField(required=False)
    email = forms.EmailField()
    subject = forms.CharField()
    messages = forms.CharField()
