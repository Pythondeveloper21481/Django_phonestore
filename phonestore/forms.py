from django.forms import ModelForm
#from django import forms


from .models import Order, Customer, Phone
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class OrderForm(ModelForm):

    class Meta:
        model = Order
        fields = "__all__"

    #fields = "__all__"
        #fields = ['customer', 'phone',  'status']
        #readonly_fields = ['date_created',]

        # widgets = {
        #      'customer': forms.TextInput(attrs={'class':'form-control'}),
        #      'phone': forms.TextInput(attrs={'class':'form-control'}),
        #      'date_created': forms.DateTimeField(),
        #      'status': forms.TextInput(attrs={'class':'form-control'}),}

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"
        exclude = ['user',]


class PhoneForm(ModelForm):
    class Meta:
        model = Phone
        fields = "__all__"

class CreateNewUser(UserCreationForm):
    class Meta:
        model = User
        #fields = "__all__"
        fields = ['username', 'email', 'password1', 'password2']

