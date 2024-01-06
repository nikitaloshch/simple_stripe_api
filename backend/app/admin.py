from django.contrib import admin
from .models import Item, Order, Discount, Tax

class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'currency')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'display_items', 'discount', 'tax', 'total_price')

    def display_items(self, obj):
        return ', '.join([item.name for item in obj.items.all()])
    display_items.short_description = 'Items'

admin.site.register(Item, ItemAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Discount)
admin.site.register(Tax)