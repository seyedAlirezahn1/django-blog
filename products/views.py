from django.shortcuts import render, get_object_or_404
from .models import Products
from django.views.generic.list import ListView

# Create your views here.

def blog_pages(request):
    products = Products.objects.all()

    context = {

        'products_list' : products

    }
    return render(request,'blog-pages.html',context)

def product_details(request, productID):
    # product = Products.objects.get(id = productID)
    product = get_object_or_404(Products, id = productID)
    context = {
        'product': product
    }

    return render(request,'blog-content.html',context)
