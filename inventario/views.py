from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Bienvenido al inventario de EcoApp!")
# Create your views here.
