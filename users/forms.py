from django import forms

from django.contrib.auth.models import User
from users.models import Profile


class ProfileForm(forms.Form):
    website = forms.URLField(max_length=200, required=True)
    biography = forms.CharField(max_length=500, required=True)
    phone_number = forms.CharField(max_length=20, required=False)
    picture = forms.ImageField()


class SignupForm(forms.Form):
    username = forms.CharField(min_length=4, max_length=50, required=True)
    password = forms.CharField(max_length=70, required=True, widget=forms.PasswordInput())
    password_confirmation = forms.CharField(max_length=70, required=True, widget=forms.PasswordInput())
    first_name = forms.CharField(min_length=4, max_length=50, required=True)
    last_name = forms.CharField(min_length=4, max_length=50, required=True)
    email = forms.CharField(min_length=4, max_length=50, required=True, widget=forms.EmailInput())

    def clean_username(self):
        username = self.cleaned_data['username']
        username_taken = User.objects.filter(username=username).exists()
        if username_taken:
            raise forms.ValidationError('Username is already in use.')
        return username

    def clean(self):
        """Verify password confirmation match."""

        data = super().clean()

        password = data['password']
        password_confirmation = data['password_confirmation']

        if password != password_confirmation:
            ex = forms.ValidationError('Passwords do not match.')
            self.add_error('password', ex)
            self.add_error('password_confirmation', ex)
            raise ex

        return data

    def save(self):
        """Create user and profile."""
        data = self.cleaned_data
        data.pop('password_confirmation')

        user = User.objects.create_user(**data)
        profile = Profile(user=user)
        profile.save()
