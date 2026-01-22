from .models import Review
from .models import Product
from django import forms


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('body',)

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'featured_image', 'content', 'status']
