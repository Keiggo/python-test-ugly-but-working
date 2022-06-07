from django.contrib import admin

from . import models


@admin.register(models.GrainsUserProfile)
class GrainsUserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'role', 'location']


@admin.register(models.Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'location', 'supply_amount']


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'purchase_order',
        'order_date',
        'customer_id',
        'customer_location',
        'amount_requested',
        'fullfilled_by_id',
        'fullfilled_by_location',
        'amount_supplied',
        'delivery_cost',
        'status'
    ]

    def customer_id(self, obj):
        return obj.customer.id

    def customer_location(self, obj):
        return obj.customer.location

    def fullfilled_by_id(self, obj):
        if obj.supplier:
            return obj.supplier.id
        return None

    def fullfilled_by_location(self, obj):
        if obj.supplier:
            return obj.supplier.location
        return None