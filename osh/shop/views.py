from django.shortcuts import render
from django.http import HttpResponse
from .models import Products
from math import ceil
# Create your views here.

def index(request):
    product=Products.objects.all()
    print(product)
    # allprod=[[product,range(1,nslide),nslide],
    #         [product,range(1,nslide),nslide]]
    ##===========================================================================##
    # dicts={"number_of_slide":nslide,"range":range(1,nslide),"product":product}
    # print(nslide)
    ##============================================================================##
    allprod=[]
    cat_products=Products.objects.values("category")
    categories={item["category"] for item in cat_products}
    for cat in categories:
        prod=Products.objects.filter(category=cat)
        n=len(product)
        nslide=n//4+ceil(n/4-n//4)
        allprod.append([prod,range(1,nslide),nslide])
    dicts={"allprod":allprod}
    return render(request,"shop/index.html",dicts)


def about(request):
    return render(request,"shop/about.html")

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
