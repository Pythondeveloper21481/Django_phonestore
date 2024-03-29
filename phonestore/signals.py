from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .models import Customer
from django.contrib.auth.models import Group
from django.core.mail import send_mail


def customer_create_profile(sender,instance, created, **kwargs):
    if created:
        group, created= Group.objects.get_or_create(name='customer')
        instance.groups.add(group)

        Customer.objects.create(
            user = instance,
            name = instance.username
        )
        print(' New Customer Profile Created! ')
        

post_save.connect(customer_create_profile, sender=User)