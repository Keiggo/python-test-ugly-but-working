from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register('users', views.GrainsUserProfileViewSet)
router.register('suppliers', views.SupplierViewSet)
router.register('orders', views.OrderViewSet)


urlpatterns = router.urls
