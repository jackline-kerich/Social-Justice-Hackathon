from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# User Registration Form
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    # Override the save method to ensure email is captured properly
    def save(self, commit=True):
        user = super(UserRegisterForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

# User Login Form
class UserLoginForm(forms.Form):
    email = forms.EmailField(label='Email', max_length=255)
    password = forms.CharField(widget=forms.PasswordInput, label='Password')

    class Meta:
        fields = ['email', 'password']
