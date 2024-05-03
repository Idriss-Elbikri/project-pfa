from django.db import models

from datetime import datetime

# Create your models here.

class Commande(models.Model):
    date = models.DateTimeField(default=datetime.now)

class Client(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    paypal = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    adresse = models.CharField(max_length=50)
    
    
class Cart(models.Model):
    x = [
        ('Dresses','Dresses'),
        ('Pants','Pants'),
        ('T-shirts','T-shirts'),
        ('Shoes','Shoes'),
        ('Jackets','Jackets'),    
    ]
    label = models.CharField(max_length=50, null=True)
    # content = models.CharField(max_length=50, null=True, blank=True)
    prix = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    # image = models.ImageField(upload_to='photos/%y/%m/%d', default='photos/24/04/30/new.jpg', null=True)
    category = models.CharField(max_length=50, choices=x,null=True)
    def __str__(self):
        return self.label

class Produit(models.Model):
    x = [
        ('Dresses','Dresses'),
        ('Pants','Pants'),
        ('T-shirts','T-shirts'),
        ('Shoes','Shoes'),
        ('Jackets','Jackets'),    
    ]
    label = models.CharField(max_length=50)
    prix = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='photos/%y/%m/%d', default='photos/24/04/30/new.jpg')
    category = models.CharField(max_length=50, null=True, blank=True, choices=x)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.label