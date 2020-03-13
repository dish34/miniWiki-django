from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

# class SignupForm(forms.Form):
#     user_name = forms.CharField(max_length=100, required=True, help_text="Enter a unique username")
#     email    = forms.EmailField(max_length=254, required=True, help_text="Required. Inform a valid email address.")
#     password = forms.CharField(widget=forms.PasswordInput(),required=True)
#     confirm_password = form.


class SignUp(UserCreationForm):
    template_name = 'scrap/signup.html'
