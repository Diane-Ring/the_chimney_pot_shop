from django.contrib import admin
from .models import Product, Review
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

@admin.register(Product)
class ProductAdmin(SummernoteModelAdmin):
    
    list_display = ('title', 'slug', 'status')
    search_fields = ['title']
    list_filter = ('status',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)

# Register your models here.

admin.site.register(Review)