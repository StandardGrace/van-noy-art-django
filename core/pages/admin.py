from django.contrib import admin
from .models import Product, Piece, Sale

# Register your models here.
admin.site.register(Product)
admin.site.register(Piece)
admin.site.register(Sale)