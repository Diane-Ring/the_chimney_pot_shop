from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Product, Review
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
            return HttpResponseRedirect(reverse('product_detail', args=[slug]))
    else:
        review_form = ReviewForm()

    reviews = product.review.all().order_by("-created_on")
    review_count = product.review.filter(approved=True).count()

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

def review_edit(request, slug, review_id):
    """
    view to edit reviews
    """
    if request.method == "POST":

        queryset = Product.objects.filter(status=1)
        product = get_object_or_404(queryset, slug=slug)
        review = get_object_or_404(Review, pk=review_id)
        review_form = ReviewForm(data=request.POST, instance=review)

        if review_form.is_valid() and review.author == request.user:
            review = review_form.save(commit=False)
            review.product = product
            review.approved = False
            review.save()
            messages.add_message(request, messages.SUCCESS, 'Review Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating review!')

    return HttpResponseRedirect(reverse('product_detail', args=[slug]))

def review_delete(request, slug, review_id):
    """
    view to delete review
    """
    queryset = Product.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    review = get_object_or_404(Review, pk=review_id)

    if review.author == request.user:
        review.delete()
        messages.add_message(request, messages.SUCCESS, 'review deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own reviews!')

    return HttpResponseRedirect(reverse('product_detail', args=[slug]))


