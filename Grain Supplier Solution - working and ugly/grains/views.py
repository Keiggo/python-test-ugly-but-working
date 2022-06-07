from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser

from . import permissions

from . import models, serializers

class GrainsUserProfileViewSet(ModelViewSet):
    queryset = models.GrainsUserProfile.objects.select_related('user').all()
    serializer_class = serializers.GrainsUserSerializer
    permission_classes = [IsAdminUser]


class SupplierViewSet(ModelViewSet):
    queryset = models.Supplier.objects.select_related('user').all()
    serializer_class = serializers.SupplierSerializer
    permission_classes = [permissions.IsSupplier]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({'request': self.request})
        return context


class OrderViewSet(ModelViewSet):
    queryset = models.Order.objects \
        .select_related('customer') \
        .select_related('supplier') \
        .select_related('broker') \
        .all()

    def get_serializer_class(self):
        if self.action in ['create', 'update']:
            return serializers.CreateOrUpdateOrderSerializer
        if self.action == 'fullfill':
            return serializers.FullfillOrderSerializer
        return serializers.OrderSerializer

    @action(methods=['PUT','GET'], detail=True)
    def fullfill(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
