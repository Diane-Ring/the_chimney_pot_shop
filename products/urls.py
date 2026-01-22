from . import views
from django.urls import path

#urlpatterns = [
#   path("", views.products, name="home"),
#]

from . import views
from django.urls import path

urlpatterns = [
     path("", views.ProductList.as_view(), name='home'),
     path('add/', views.add_product, name='add_product'),
     path('<slug:slug>/', views.product_detail, name='product_detail'),
     path('<slug:slug>/edit_review/<int:review_id>',
         views.review_edit, name='review_edit'),
     path('<slug:slug>/delete_review/<int:review_id>',
         views.review_delete, name='review_delete'),
]