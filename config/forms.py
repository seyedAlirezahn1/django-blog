from django import forms
from django.contrib.auth import get_user_model

user = get_user_model()

class Loginform(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder":"enter your username"})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder":"enter your password"})
    )

class Rigesterform(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder":"enter your username"})
    )
    email = forms.EmailField(
        widget=forms.TextInput(attrs={"placeholder":"enter your email"})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder":"enter your password"})
    )
    password2 = forms.CharField(
        label="confrim password",
        widget=forms.PasswordInput(attrs={"placeholder":"enter your password again"})
    )

    def clean_username(self):
        username = self.cleaned_data.get("username")
        query = user.objects.filter(username = username)

        if query.exists():
            raise forms.ValidationError("this username is bloked")
        return username

    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")
        if password!=password2:
            raise forms.ValidationError("password is not match")
        return data