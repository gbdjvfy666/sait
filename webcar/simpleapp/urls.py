from django.urls import path
from .views import ProductsList,ProductDetails
from simpleapp.views import index

urlpatterns = [
    path('', ProductsList.as_view()),
    path('index', index),
    path('int:pk', ProductDetails.as_view()),
]