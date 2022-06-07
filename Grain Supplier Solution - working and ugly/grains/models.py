from uuid import uuid4
from django.db import models
from django.conf import settings

from . import constants

class GrainsUserProfile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    location = models.CharField(max_length=255, blank=True, null=True)
    role = models.CharField(max_length=20, choices=constants.ROLE)

    class Meta:
        verbose_name = 'Grains User Profile'

    def __str__(self) -> str:
        return str(self.user.email)

class Supplier(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    user = models.ForeignKey(GrainsUserProfile, on_delete=models.CASCADE, related_name='suppliers')
    location = models.CharField(max_length=255)
    supply_amount = models.PositiveIntegerField()

    def __str__(self) -> str:
        return str(self.user.user.email)


class Order(models.Model):
    purchase_order = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    order_date = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(GrainsUserProfile, on_delete=models.CASCADE, related_name='orders')
    amount_requested = models.PositiveIntegerField()
    broker = models.ForeignKey(GrainsUserProfile, on_delete=models.CASCADE, related_name='fullfilled_orders', blank=True, null=True)
    fullfilled_date = models.DateTimeField(auto_now=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name='orders', blank=True, null=True)
    amount_supplied = models.PositiveIntegerField(blank=True, null=True)
    delivery_cost = models.DecimalField(decimal_places=2, max_digits=52, blank=True, null=True)
    status = models.CharField(max_length=20, choices=constants.ORDER_STATUS, default=constants.PENDING)

    def __str__(self) -> str:
        return str(self.purchase_order)
