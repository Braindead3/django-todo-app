from django.contrib.auth.forms import UserCreationForm
from .models import UserAccount


class RegisterForm(UserCreationForm):
    class Meta:
        model = UserAccount
        fields = ['email', 'user_name', 'password1', 'password2']
