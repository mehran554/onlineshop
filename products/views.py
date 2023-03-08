from django.shortcuts import render, get_object_or_404
from django.views import generic

from .models import Product, Comments
from .forms import CommentForm
from cart.forms import FormAddProductToCart


class ProductListView(generic.ListView):
    queryset = Product.objects.filter(active=True)
    template_name = 'products/product_list.html'
    context_object_name = 'products'


class ProductListDetails(generic.DetailView):
    model = Product
    template_name = 'products/product_details.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_comment'] = CommentForm()
        # context['add_to_cart_form'] = FormAddProductToCart()
        return context


class CommentCreateView(generic.CreateView):
    model = Comments
    form_class = CommentForm

    def form_valid(self, form):
        # new_form = super().form_valid(form)
        new_form = form.save(commit=False)
        new_form.author = self.request.user
        product_id = int(self.kwargs['product_id'])
        product = get_object_or_404(Product, id=product_id)
        new_form.product = product
        return super().form_valid(form)
