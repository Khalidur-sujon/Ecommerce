from django.shortcuts import render
from products.models import Product


def home_page(request):
    context = {'products': Product.objects.all()}
    return render(request, 'home/home_page.html', context)
