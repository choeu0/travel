from django import forms

class AddCityForm(forms.Form):
    is_update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)