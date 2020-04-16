from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.models import User, auth
import pyrebase

config = {
    'apiKey': "AIzaSyDBqgNKO2Z9P3jU1JZjKSCRFPk8wlHpibQ",
    'authDomain': "sorting-visualizer-efc1c.firebaseapp.com",
    'databaseURL': "https://sorting-visualizer-efc1c.firebaseio.com",
    'projectId': "sorting-visualizer-efc1c",
    'storageBucket': "sorting-visualizer-efc1c.appspot.com",
    'messagingSenderId': "789464817660",
    'appId': "1:789464817660:web:8e23804e85528cd25b1c79",
    'measurementId': "G-NPV6N1FYJZ"
}

firebase = pyrebase.initialize_app(config)

auth = firebase.auth()


# Create your views here.
class home(TemplateView):
    template_name = 'index.html'





