from django.shortcuts import render
from django.http import HttpResponse
from cubecrafty.models import *
# Create your views here.

def index(request):
    all_cubes = Cube.objects.all()
    return render(request, 'index.html', {
        "all_cubes": all_cubes,
        })

def categories(request):
    return render(request, 'categories.html', {
        })

def crafty_cubes(request):
    crafty_cubes = Cube.objects.filter(is_custom=True)
    return render(request, 'crafty_cubes.html', {
        "crafty_cubes": crafty_cubes,
        })

def basic_cubes(request):
    basic_cubes = Cube.objects.filter(is_custom=False)
    return render(request, 'basic_cubes.html', {
        "basic_cubes": basic_cubes,
        })

def cart(request):
    return render(request, 'cart.html', {
        })

def checkout(request):
    return render(request, 'checkout.html', {
        })

def confirmation(request):
    return render(request, 'confirmation.html', {
        })
