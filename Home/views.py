from django.shortcuts import render
from . models import Home
from django.views.generic import ListView
# Create your views here.

class HomeList(ListView):
    model = Home