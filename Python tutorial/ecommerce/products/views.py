from django.http import HttpResponse
from django.shortcuts import render
from .models import Product

# We have to map localhost.../product to index
# We are going to set it in the 
# products/urls.py file

# Web page views by URL 
def index(request):
    products = Product.objects.all()    # {'products': products} -> context to use in the template
    return render(request, 'index.html',{'products': products}) 

#That would be our localhost.../product/new
def product_new(request):
    return HttpResponse('Hello new word')

def product_offer(request):
    return HttpResponse('Offer view webviews')
    