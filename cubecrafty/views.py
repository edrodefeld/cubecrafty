from django.shortcuts import render, redirect
from django.http import HttpResponse
from cubecrafty.models import *

# Create your views here.

def index(request):
    all_cubes = Cube.objects.all()
    return render(request, 'index.html', {
        "all_cubes": all_cubes,
        })

def categories(request, category):
    cubes = Cube.objects.filter(category=category)
    return render(request, 'categories.html', {
                    'cubes': cubes,
                    'category': category,
        })

def product(request, product):
    cube = Cube.objects.get(slug=product)
    return render(request, 'product.html', {
                    'cube': cube,
    })

def added(request, product):
    if request.session.get('cubes', []):
        request.session['cubes'].append(product)
        request.session.modified = True
    else:
        request.session['cubes'] = [product]
    return redirect('/cart/')

def deleted(request, product):
    if request.session.get('cubes', []):
        request.session['cubes'].remove(product)
        request.session.modified = True
    else:
        request.session['cubes'] = []
    return redirect('/cart/')

def cart(request):
    slugs = request.session.get('cubes', [])
    cubes = []
    total = 0.0
    for slug in slugs:
        cube = Cube.objects.get(slug=slug)
        cubes.append(cube)
        total += float(cube.price)
    return render(request, 'cart.html', {
                    'cubes': cubes,
                    'total': total,
        })

def checkout(request):
    slugs = request.session.get('cubes', [])
    cubes = []
    total = 0.0
    for slug in slugs:
        cube = Cube.objects.get(slug=slug)
        cubes.append(cube)
        total += float(cube.price)
    return render(request, 'checkout.html', {
            'cubes': cubes,
            'total': total,
        })

def confirmation(request):
    return render(request, 'confirmation.html', {
        })
