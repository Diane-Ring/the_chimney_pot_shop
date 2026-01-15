from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
from .models import Product
from .forms import ReviewForm

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
    reviews = product.review.all().order_by("-created_on")
    review_count = product.review.filter(approved=True).count()

    if request.method == "POST":
        review_form = ReviewForm(data=request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.author = request.user
            review.product = product
            review.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Review submitted and awaiting approval'
    )

    else:
        review_form = ReviewForm()

    return render(
        request,
        "products/product_detail.html",
        {
            "product": product,
            "reviews": reviews,
            "reviews_count": review_count,
            "review_form": review_form,
        },
    )
