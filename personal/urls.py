from django.conf.urls import url
from . import views
from django.urls import path

from .views import home

urlpatterns = [
    path('', home.as_view(), name='home'),  # new

]
