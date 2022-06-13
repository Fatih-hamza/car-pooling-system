from django.forms import ModelForm
from .models import User
from django import forms



class UserForm(ModelForm):

    password1 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                  # 'class': 'form-control',
                                                                  # 'data-toggle': 'password',
                                                                  'id': 'password',
                                                                  }))
# we added the id attribute to the password field because we will need it with the plugin og the show/hide icon 
    password2 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password',
                                                                  # 'class': 'form-control',
                                                                  # 'data-toggle': 'password',
                                                                  'id': 'password',
                                                                  }))
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'date_naissance', 'number', 'email', 'nature', 'password1', 'password2']








