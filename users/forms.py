from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django.utils.translation import ugettext_lazy as _


class LoginForm(forms.Form):
    username = forms.CharField(max_length=255, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if not user:
            raise forms.ValidationError("Usuário ou senha inválida.")
        elif not user.is_active:
            raise forms.ValidationError(
                "Usuário inativo, entre em contato com o admin do sistema."
            )
        return self.cleaned_data

    def login(self, request):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        return user


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(
        help_text=_('*Obrigatório. 30 caracteres ou menos. Somente letras, dígitos e @/./+/-/_.'),
        required=True,
        widget = forms.TextInput(attrs={'placeholder': 'Nome de usuário'}),
    )
    email = forms.EmailField(
        help_text=_('*Obrigatório'),
        required=True,
        widget = forms.TextInput(attrs={'placeholder': 'Email'}),
    )
    first_name = forms.CharField(
        label = _('Nome'),
        widget = forms.TextInput(attrs={'placeholder': 'Nome'}),
        help_text=_('*Obrigatório, no máximo 100 caracteres'),
        max_length=100,
        required=True
    )
    last_name = forms.CharField(
        label = _('Sobrenome'),
        widget = forms.TextInput(attrs={'placeholder': 'Sobrenome'}),
        help_text=_('*Obrigatório, no máximo 100 caracteres'),
        max_length=100,
        required=True
    )
    password1 = forms.CharField(
        label = _('Senha'),
        widget = forms.PasswordInput(attrs={'placeholder': 'Senha'}),
        required = True
    )
    password2 = forms.CharField(
        label = _('Confirmação de senha'),
        widget = forms.PasswordInput(attrs={'placeholder': 'Confirmação de senha'}),
        required = True
    )

    class Meta:
        model = User
        fields = (
            'username', 'email', 'first_name', 'last_name', 'password1',
            'password2',
        )

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Este e-mail já está em uso.')
        return email

    def save(self, commit=True):
        user = super(RegisterUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
        return user
