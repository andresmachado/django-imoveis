from django.http import *
from django.shortcuts import render, render_to_response, redirect
from django.contrib import messages
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse

from .forms import RegisterUserForm

def login_user(request, template_name='users/login.html'):
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                messages.success(request, "Bem vindo, {}".format(request.user.username))
                return HttpResponseRedirect(reverse('index'))
            else:
                messages.error(request, "Seu usuário está inativo, favor entrar em contato com o administrador.")
                return HttpResponseRedirect(reverse('index'))
    return render(request, template_name, context_instance=RequestContext(request))


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