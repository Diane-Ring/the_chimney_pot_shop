from django.shortcuts import render
from django.views import generic
from .models import Product

#class HomePage(TemplateView):
"""
 Displays home page"
"""
#   template_name = 'index.html'

# Create your views here.
class ProductList(generic.ListView):
    model = Product