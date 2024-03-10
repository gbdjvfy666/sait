from django.shortcuts import render
from datetime import datetime
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView
from django.contrib.auth.mixins import PermissionRequiredMixin
from .forms import ProductForm
from .models import Product
from .filters.filters import ProductFilter
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class ProductCreate(LoginRequiredMixin, CreateView):
    raise_exception = True
    form_class = ProductForm
    model = Product
    template_name = 'prodict_edit.html'


# Create your views here.

class ProductsList(ListView):
    model = Product
    ordering = 'name'
    template_name = 'products.html'
    context_object_name = 'products'
    paginate_by = 2

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = ProductFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['next_sale'] = "Распродажа в среду"
        return context


class ProductDetails(DetailView):
    model = Product
    template_name = 'product.html'
    context_object_name = 'product'


class ProductCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('simpleapp.add_product',)
    form_class = ProductForm
    model = Product
    template_name = 'product_edit.html'


class ProductDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ('simpleapp.add_product',)
    model = Product
    template_name = 'product_delete.html'
    success_url = reverse_lazy('product_list')


class ProductUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = ('simpleapp.add_product',)
    form_class = ProductForm
    model = Product
    template_name = 'product_edit.html'


def index(request):
    return render(request, 'index.html')
