from django.urls import path

from . import views

urlpatterns = [
    path("register", views.register, name="register"),
    path("signIn", views.signIn, name="signIn"),
    path("signOut", views.signOut, name="signOut")

]