from django.shortcuts import render, redirect
from django.http import HttpResponse
from OHSIHA_app.models import *

def home(request):
    return render(request, "home.html")
