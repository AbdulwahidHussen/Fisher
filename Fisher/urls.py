from django.urls import path
from .views import *
urlpatterns = [
    path('login', login, name='login'),
    path('register', register, name='register'),
    path('dashboard', dashboard, name='dashboard'),
path('order', Userorder, name='Userorder'),
    path('<str:url>', redirectto, name='redirectto'),
    path('logout', log_out, name='logout'),


]