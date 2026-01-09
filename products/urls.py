from . import views
from django.urls import path

#urlpatterns = [
#   path("", views.products, name="home"),
#]

urlpatterns = [
    path("",views.HomePage.as_view(),name='home')
]