from django.shortcuts import render, HttpResponse
from math import ceil
from .models import *
# Create your views here.

def index(request):
    allProds = []
    catprods = product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])
    params={'allProds':allProds }
    return render(request, "ecom/index.html", params)
    # products = product.objects.all()
    # n = len(products)
    # nSlides = ceil(n/4)
    # allProds=[[products, range(1, len(products)), nSlides],[products, range(1, len(products)), nSlides]]

def about(request):
    return HttpResponse("Buckler")

def contact(request):
    return HttpResponse("Buckler")

def tracker(request):
    return HttpResponse("Buckler")

def search(request):
    return HttpResponse("Buckler")

def productView(request):
    return HttpResponse("Buckler")

def checkOut(request):
    return HttpResponse("Buckler")