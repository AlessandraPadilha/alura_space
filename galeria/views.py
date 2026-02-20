from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Olá! Esta é a cara nova do meu servidor.</h1>")