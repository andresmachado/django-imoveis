from django.http import *
from django.shortcuts import render, get_object_or_404
from django.template import RequestContext
from django.core.exceptions import PermissionDenied
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse

from .forms import RegisterUserForm, LoginForm
from properties.models import Property

def login_user(request, template_name='users/login.html'):
    form = LoginForm(request.POST or None)
    if request.POST and form.is_valid():
        user = form.login(request)
        if user:
            login(request, user)
            messages.success(request, "Bem vindo, {}".format(request.user.username))
            return HttpResponseRedirect(reverse('index'))
    return render(request, 'users/login.html', {'login_form': form})

def logout_user(request):
	if request.user.is_authenticated():
		logout(request)
		messages.success(request, "Logout realizado com sucesso!")
		return HttpResponseRedirect(reverse('index'))
	else:
		raise Http404

def register(request, template_name='users/signup.html'):
    form = RegisterUserForm()
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            request.session['registered'] = True
            return HttpResponseRedirect(reverse('registration_complete'))
    return render(request, template_name, {'form': form})


def registration_complete(request):
    if request.session.get('registered', True):
        request.session['registered'] = False
        return render(request, 'users/registration_complete.html')
    else:
        raise Http404

@login_required
def user_profile(request):
    user = get_object_or_404(User, username=request.user.username)
    my_properties = Property.objects.filter(owner=request.user.id)
    context = {
        'user': user,
        'properties': my_properties
    }
    return render(request, 'users/my_account_properties.html', context)

@login_required
def user_profile_settings(request, template_name="users/my_account_settings.html"):
    user = get_object_or_404(User, username=request.user.username)
    return render(request, template_name, {'user': user})