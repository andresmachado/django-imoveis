from django.conf.urls import url, include
from django.contrib.auth.views import password_reset, password_reset_done
from django.contrib import admin

from users import views
from properties.views import property_delete

urlpatterns = [
    url(r'^login/$', views.login_user, name='login_user'),
    url(r'^logout/$', views.logout_user, name='logout_user'),
    url(r'^accounts/register/$', views.register, name='register'),
    url(r'^accounts/register/complete/$', views.registration_complete, name='registration_complete'),
    url(r'^myaccount/home/$', views.user_profile, name='user_profile'),
    url(r'^myaccount/home/settings/$', views.user_profile_settings, name='user_settings'),
    url(r'^myaccount/home/imoveis/excluir/$', property_delete),
]