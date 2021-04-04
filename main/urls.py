from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('login', loginPage, name='login'),
    path('register', RegistrationView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
]
