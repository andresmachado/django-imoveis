from django.http import *
from django.shortcuts import render, render_to_response, redirect
from django.contrib import messages
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse

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
    return render(request, template_name, context_instance=RequestContext(request))


def logout_user(request):
	if request.user.is_authenticated():
		logout(request)
		messages.success(request, "Logout realizado com sucesso!")
		return HttpResponseRedirect(reverse('index'))
	else:
		raise Http404
		# messages.error(request, "Você não está logado!")
		# return render(request, 'properties/index.html')

def register(request):
    pass