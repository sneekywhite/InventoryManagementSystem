from django.contrib import admin
from .models import Supplier, Item



@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ["name","description","price","quantity", "date_added"]
    list_filter = ["date_added"]

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ["name","supplier_email","supplier_phone"]
    list_filter = ["name"]
