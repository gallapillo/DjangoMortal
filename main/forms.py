from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, forms, TextInput, PasswordInput, CharField


class LoginForm(ModelForm):
    pass


class RegisterUserForm(UserCreationForm):
    username = CharField(widget=TextInput(
        attrs={'class': 'form-input', 'placeholder': 'Имя пользователя',
               'style': 'padding:10px 25px; font-size: 16px; line-height: 20px;'}))
    password1 = CharField(label='Пароль', widget=PasswordInput(
        attrs={'class': 'form-input', 'placeholder': 'Пароль',
               'style': 'padding:10px 25px; font-size: 16px; line-height: 20px;'}))
    password2 = CharField(label='Повторите пароль', widget=PasswordInput(
        attrs={'class': 'form-input', 'placeholder': 'Подтвердите пароль',
               'style': 'padding:10px 25px; font-size: 16px; line-height: 20px;'}))

    class Meta:
        model = User
        # fields = ('username', 'password1', 'password2')
        # widgets = {'username': TextInput(attrs={'class': 'form-input', 'placeholder': 'Имя пользователя', }),
        # 'password1': PasswordInput(attrs={'class': 'form-input'}),'password2': PasswordInput(attrs={'class':
        # 'form-input'}),}
        fields = UserCreationForm.Meta.fields + ('username', 'password1', 'password2',)


class LoginUserForm(AuthenticationForm):
    username = CharField(widget=TextInput(
        attrs={'class': 'form-input', 'placeholder': 'Имя пользователя',
               'style': 'padding:10px 25px;  font-size: 16px; line-height: 20px;'}))
    password = CharField(label='Пароль', widget=PasswordInput(
        attrs={'class': 'form-input', 'placeholder': 'Пароль',
               'style': 'padding:10px 25px; font-size: 16px; line-height: 20px;'}))

    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ('username', 'password',)
