"""Urls of registration app."""
from django.urls import path

from registration import views

app_name = 'registration'
urlpatterns = [
    path("", views.index, name='index'),
    path("signup/", views.signup, name='signup'),
    path("login/", views.login, name='login'),
    path("logout/", views.logout_user, name="logout"),
    path("home/<str:username>", views.home, name='home'),

]