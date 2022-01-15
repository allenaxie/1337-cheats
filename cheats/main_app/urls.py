from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
     path('accounts/sign_up/', views.signup, name='signup'),
]