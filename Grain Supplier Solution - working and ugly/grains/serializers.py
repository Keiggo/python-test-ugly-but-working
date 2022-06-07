from django.contrib.auth import get_user_model
from django.http import request
from rest_framework.serializers import ModelSerializer, ValidationError, CharField, EmailField, SerializerMethodField

from . import models, constants


class UserSerializer(ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'first_name', 'last_name', 'email']


class GrainsUserSerializer(ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = models.GrainsUserProfile
        fields = '__all__'

    def create(self, validated_data):
        raise ValidationError('Not Implemented')


class SupplierSerializer(ModelSerializer):
    class Meta:
        model = models.Supplier
        fields = ['id', 'location', 'supply_amount', 'user']
        read_only_fields = ['user']

    def create(self, validated_data):
        user = self.context['request'].user
        user_profile = models.GrainsUserProfile.objects.filter(user__email=user.email).first()
        validated_data['user'] = user_profile
        return super().create(validated_data)


class OrderSerializer(ModelSerializer):
    class Meta:
        model = models.Order
        fields = [
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
    customer_id = SerializerMethodField('get_customer_id')
    customer_location = SerializerMethodField('get_customer_location')
    fullfilled_by_id = SerializerMethodField('get_fullfilled_by_id', required=False)
    fullfilled_by_location = SerializerMethodField('get_fullfilled_by_location')

    def get_customer_location(self, obj):
        return obj.customer.location

    def get_customer_id(self, obj):
        return obj.customer.id

    def get_fullfilled_by_id(self, obj):
        if obj.supplier:
            return obj.supplier.id
        return None

    def get_fullfilled_by_location(self, obj):
        if obj.supplier:
            return obj.supplier.location
        return None



class CreateOrUpdateOrderSerializer(OrderSerializer):
    class Meta:
        model = models.Order
        fields = [
            'purchase_order',
            'order_date',
            'customer',
            'customer_id',
            'customer_location',
            'amount_requested',
            'fullfilled_by_id',
            'fullfilled_by_location',
            'amount_supplied',
            'delivery_cost',
            'status'
        ]
        read_only_fields = [
            'purchase_order',
            'order_date',
            'customer_id',
            'customer_location',
            'fullfilled_by',
            'fullfilled_by_location',
            'amount_supplied',
            'delivery_cost',
            'status'
        ]

    def validate(self, attrs):
        data = dict(attrs)
        user = data.get('customer')
        if user and user.role != constants.CUSTOMER:
            raise ValidationError('only customers can create or modify orders')
        return super().validate(attrs)

    def update(self, instance, validated_data):
        if instance.status == constants.FULLFILLED and validated_data:
            raise ValidationError('order already fullfilled')
        return super().update(instance, validated_data)


class FullfillOrderSerializer(OrderSerializer):
    class Meta:
        model = models.Order
        fields = [
            'supplier',
            'amount_supplied',
            'delivery_cost',
            'broker',
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
        read_only_fields = [
            'purchase_order',
            'order_date',
            'customer_id',
            'customer_location',
            'amount_requested',
            'fullfilled_by_id',
            'fullfilled_by_location',
            'status'
        ]

    def validate(self, attrs):
        data = dict(attrs)
        broker = data.get('broker')
        if broker and broker.role != constants.BROKER:
            raise ValidationError('only brokers can fullfill orders')
        return super().validate(attrs)

    def update(self, instance: models.Order, validated_data):
        if instance.status == constants.FULLFILLED and validated_data:
            raise ValidationError('order already fullfilled')

        if validated_data:
            print(validated_data)
            supplier: models.Supplier = validated_data.get('supplier')
            amount_supplied = validated_data.get('amount_supplied')
            amount_requested = instance.amount_requested
            supply_amount = supplier.supply_amount
            if amount_supplied > supply_amount:
                raise ValidationError('amount_supplied cannot be greater than supply_amount')
            if amount_supplied > amount_requested:
                raise ValidationError('amount_supplied cannot be greater than amount_requested')
            if amount_supplied < 1:
                raise ValidationError('amount_supplied cannot be lower than 1')
            if supply_amount-amount_supplied > 0:
                models.Supplier.objects.filter(pk=supplier.id).update(supply_amount=supply_amount-amount_supplied)
            validated_data['status'] = constants.FULLFILLED
        return super().update(instance, validated_data)



