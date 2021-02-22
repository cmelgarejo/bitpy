from django import forms


class ShrtForm(forms.Form):
    url = forms.CharField(max_length=1024,
                          widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "URL to shrt"}))
