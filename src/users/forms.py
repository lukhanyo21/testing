from django import forms
from django.contrib.auth.models import User

# from .models import OpsUser

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        # model = OpsUser
        fields = ['first_name', 'last_name']