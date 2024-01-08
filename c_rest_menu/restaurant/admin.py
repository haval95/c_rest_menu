from django.contrib import admin
from .models import menu_item, category, order


admin.site.register(menu_item)
admin.site.register(category)
admin.site.register(order)
