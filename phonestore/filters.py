import django_filters
from .models import Order, Customer, Phone


class OrderFilter(django_filters.FilterSet):
    

    class Meta:
        model = Order
        fields = ['phone', 'status', 'customer',]
        exclude = ['customer']

    widgets = {
                  'phone': django_filters.CharFilter(attrs={'class':'form-control'}),
                  'status': django_filters.CharFilter(attrs={'class':'form-control'}),
                }