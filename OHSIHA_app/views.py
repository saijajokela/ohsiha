from django.shortcuts import render, redirect
from django.http import HttpResponse
from OHSIHA_app.models import *
from django.shortcuts import render
import requests

def home(request):
    return render(request, "home.html"),

def index(request):

    response = requests.get('http://api.teosto.fi/2017/event')
    tapahtumat = response.json()
    return render(request, 'etusivu.html', {
        'tapahtumalista': tapahtumat['name']
    })
