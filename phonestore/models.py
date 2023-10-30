from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True)
    email =models.EmailField(max_length=150, null=True)
    phone = models.CharField(max_length=100, null=True)
    age = models.CharField(max_length=100, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    photo = models.ImageField(blank=True, null=True, default='wallpaper1.jpg')

    def __str__(self) :
        return (self.name)
    
class Tag(models.Model):
    marque = models.CharField(max_length=100, null=True)
    def __str__(self) :
        return (self.marque)

    

    
class Phone(models.Model):

    STATUS ={
        
        ('availabe', 'availabe'),
        ('Out of order', 'Out of order'),

        }

    marque = models.CharField(max_length=100, null=True)
    model = models.CharField(max_length=100, null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=100, null=True)
    tags = models.ManyToManyField(Tag)
    description = models.CharField(max_length=100, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    photo = models.ImageField(null=True)
    status = models.CharField(max_length=100, null=True, choices=STATUS)

    def __str__(self) :
        return (self.marque)
    

    
class Order(models.Model):
    STATUS ={
        
        ('pending', 'pending'),
        ('delivred', 'delivred'),
        ('in progress', 'in progress'),
        ('Out of order', 'Out of order'),

        }
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    phone = models.ForeignKey(Phone, null=True, on_delete=models.SET_NULL)
    tags = models.ManyToManyField(Tag)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=100, null=True, choices=STATUS)

    def __str__(self) :
        return self.status
    
