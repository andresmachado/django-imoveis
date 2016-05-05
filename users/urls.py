"""django_imoveis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from . import views

urlpatterns = [
    # url(r'^login/$', views.login_user, name='login_user'),
    # url(r'^logout/$', views.logout_user, name='logout_user'),
    # url(r'^accounts/register/$', views.register, name='register'),
    # url(r'^accounts/register/complete/$', views.registration_complete, name='registration_complete'),
    # url(r'^myaccount/home/(?P<pk>[0-9]+)/$', views.user_profile, name='user_profile'),
    # url(r'^myaccount/home/(?P<pk>[0-9]+)/myposts/$', views.user_posts, name='user_posts'),
]