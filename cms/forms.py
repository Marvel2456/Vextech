from django.forms import ModelForm
from django import forms
from .models import CustomUser
from django.core.exceptions import ValidationError


class CustomUserCreationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password1 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
    terms = forms.BooleanField(required=True)

    class Meta:
        model = CustomUser
        fields = ['email', 'name']
        
    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password1 = self.cleaned_data.get('password1')
        
        if password and password1 and password != password1:
            raise ValidationError("Passwords don't match")
        return password1

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user