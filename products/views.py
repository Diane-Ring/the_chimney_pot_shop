from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

class HomePage(TemplateView):
    """
    Displays home page"
    """
    template_name = 'index.html'

# Create your views here.
def products(request):
    return HttpResponse("Products")