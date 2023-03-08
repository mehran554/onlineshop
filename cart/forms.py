from django import forms


class FormAddProductToCart(forms.Form):
    QUANTITY_CHOICES = ((i, str(i)) for i in range(1, 31))
    quantity = forms.TypedChoiceField(choices=QUANTITY_CHOICES, coerce=int)
    is_add = forms.BooleanField(required=False, widget=forms.HiddenInput)
