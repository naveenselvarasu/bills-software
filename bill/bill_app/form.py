from bill_app.models import Store_add
from django import forms


class data(forms.ModelForm):
    class Meta:
        model = Store_add
        fields = ['Name_of_Product', 'Price', 'Discount']

