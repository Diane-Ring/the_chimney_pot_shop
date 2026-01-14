from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Product

#class HomePage(TemplateView):
"""
 Displays home page"
"""
#   template_name = 'index.html'

# Create your views here.
class ProductList(generic.ListView):
    queryset = Product.objects.filter(status=1).order_by("-created_on")
    template_name = "products/index.html"
    paginate_by = 6

def product_detail(request, slug):
    """
    Display an individual :model:`products.Product`.

    **Context**

    ``product``
        An instance of :model:`products.Product`.

    **Template:**

    :template:`products/product_detail.html`
    """

    queryset = Product.objects.filter(status=1)
    product = get_object_or_404(queryset, slug=slug)
    return render(
        request,
        "products/product_detail.html",
        {"product": product},
    )
