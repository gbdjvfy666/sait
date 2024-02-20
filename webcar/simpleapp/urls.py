from django.urls import path
from .views import (
    ProductsList, ProductDetails, ProductCreate, ProductUpdate, ProductDelete
)
from .views import index

urlpatterns = [
    path('', ProductsList.as_view()),
    path('index', index),
    path('int:pk', ProductDetails.as_view()),
    path('', ProductsList.as_view(), name='product_list'),
    path('<int:pk>', ProductDetails.as_view(), name='product_detail'),
    path('create/', ProductCreate.as_view(), name='product_create'),
    path('<int:pk>/update/', ProductUpdate.as_view(), name='product_update'),
    path('<int:pk>/delete/', ProductDelete.as_view(), name='product_delete'),
    path('<int:pk>/create/', ProductCreate.as_view(), name='product_create'),
]