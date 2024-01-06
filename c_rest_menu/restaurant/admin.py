from django.contrib import admin
from .models import menu_item, category, order, ordered_item


admin.site.register(menu_item)
admin.site.register(category)
admin.site.register(order)
admin.site.register(ordered_item)
