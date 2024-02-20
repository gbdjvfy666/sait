from django.shortcuts import render
from datetime import datetime
from django.views.generic import ListView, DetailView
from .models import Product


# Create your views here.

class ProductsList(ListView):
    model = Product
    ordering = 'name'
    template_name = 'products.html'
    context_object_name = 'products'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['next_sale'] = "Распродажа в среду"
        return context


class ProductDetails(DetailView):
    model = Product
    template_name = 'product.html'
    context_object_name = 'product'


def index(request):
    return render(request, 'index.html')
