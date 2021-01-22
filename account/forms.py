from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm

class DecisonMakerSignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_decisonmaker = True

        if commit:
            user.save()
        return user

class FarmerSignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields =  ("username", "email", "first_name", "last_name", "phone_number",  "password1", "password2")
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_farmer = True

        if commit:
            user.save()
        return user
