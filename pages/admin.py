from django.contrib import admin

from .models import Produit,Commande,Client,Cart
# Register your models here.

admin.site.register(Produit)
admin.site.register(Commande)
admin.site.register(Client)
admin.site.register(Cart)
