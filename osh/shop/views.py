from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request,"shop/index.html")

def about(request):
    return HttpResponse("About Us")

def contact(request):
    return HttpResponse("Contact US")

def track(request):
    return HttpResponse("Track Your Products")

def search(request):
    return HttpResponse("Search")

def products(request):
    return HttpResponse("Products View")

def checkout(request):
    return HttpResponse("Checkout Page")
