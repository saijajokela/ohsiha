from django.shortcuts import render, redirect
from django.http import HttpResponse
from OHSIHA_app.models import *
from django.shortcuts import render
import requests

def home():
    return render("home.html")

def datasivu(request):
    response = requests.get('http://api.teosto.fi/2017/event/')
    tapahtumat = response.json()
    return render(request, 'datasivu.html', {
        'tapahtumalista': tapahtumat['events']})
