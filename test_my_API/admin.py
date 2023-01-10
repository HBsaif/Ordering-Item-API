from django.contrib import admin
from .models import Item, CharityRegistration, UserRegistration, OrderItem
# Register your models here.

admin.site.register(Item)
admin.site.register(CharityRegistration)
admin.site.register(UserRegistration)
admin.site.register(OrderItem)