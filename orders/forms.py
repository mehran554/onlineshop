from django import forms
from .models import Order
from django.utils.translation import gettext as _


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'phone_number', 'address', 'order_note', ]

        widgets = {
            'address': forms.Textarea(attrs={'rows': 3}),
            'order_note': forms.Textarea(
                attrs={'rows': 8, 'placeholder': _('if you have any notes please enter here Otherwise leave it empty ')})
        }
