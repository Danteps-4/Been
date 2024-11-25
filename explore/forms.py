from django import forms

class AddVisitForm(forms.Form):
    country = forms.CharField()