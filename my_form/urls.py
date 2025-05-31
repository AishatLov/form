from django.urls import path
from . import views

urlpatterns = [
    # Add any additional URL patterns here if needed.
    path("login", views.signIn, name="login"),
    path('register', views.createAccount, name="register"),
]