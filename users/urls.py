from django.conf.urls import url

from properties.views import property_delete

from users import views

urlpatterns = [
    url(r'^login/$', views.login_user, name='login_user'),
    url(r'^logout/$', views.logout_user, name='logout_user'),
    url(r'^accounts/register/$', views.register, name='register'),
    url(r'^accounts/register/complete/$', views.registration_complete, name='registration_complete'),
    url(r'^myaccount/home/$', views.user_profile, name='user_profile'),
    url(r'^myaccount/home/settings/$', views.user_settings, name='user_settings'),
    url(r'^myaccount/home/imoveis/excluir/$', property_delete),
]
