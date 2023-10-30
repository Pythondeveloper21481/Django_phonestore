from django.contrib import admin
from .models import Customer, Order, Phone, Tag
# Register your models here.

admin.site.register(Customer)
admin.site.register(Phone)
admin.site.register(Order)
admin.site.register(Tag)
