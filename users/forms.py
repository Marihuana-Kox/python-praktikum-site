from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms


User = get_user_model()


# создадим собственный класс для формы регистрации
# сделаем его наследником предустановленного класса UserCreationForm
class CreationForm(UserCreationForm):
    email = forms.EmailField(required=True,)

    class Meta(UserCreationForm.Meta):
        # модель уже существует, сошлёмся на неё
        model = User
        # укажем, какие поля должны быть видны в форме и в каком порядке
        fields = ("first_name", "last_name", "username", "email")
