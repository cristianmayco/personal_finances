from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm


class RegisterUserForm(UserCreationForm):
    name = forms.CharField(required=True)
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = (
            'name',
            'email',
            'password1',
            'password2'
        )

    def save(self, commit=True):
        user = super(RegisterUserForm, self).save(commit=False)
        user.name = self.cleaned_data['name']

        if commit:
            user.save()

        return user
