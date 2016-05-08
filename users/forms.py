from django import forms
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterUserForm(UserCreationForm):
	email = forms.EmailField(help_text=_('*Obrigatório'), required=True)
	first_name = forms.CharField(help_text=_('*Obrigatório, no máximo 100 caracteres'), max_length=100, required=True)
	last_name = forms.CharField(help_text=_('*Obrigatório, no máximo 100 caracteres'), max_length=100, required=True)

	class Meta:
		model = User
		fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2', )

	def save(self, commit=True):
		user = super(RegisterUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		user.first_name = self.cleaned_data['first_name']
		user.last_name = self.cleaned_data['last_name']
		if commit:
			user.save()
		return user
