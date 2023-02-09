from django.shortcuts import render, get_object_or_404
from django.utils.translation import gettext as _
from django.views import generic
from django.contrib import messages
from .models import Product, Comments
from .forms import CommentForm


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
        messages.success(self.request, _('Message Success'))
        # messages.success(self.request, 'موفقیت آمیز!!!')
        return super().form_valid(form)
