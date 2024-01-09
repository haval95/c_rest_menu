from django.contrib import admin
from .models import Menu_item, Category, Order, Ordered_item


admin.site.register(Menu_item)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(Ordered_item)
