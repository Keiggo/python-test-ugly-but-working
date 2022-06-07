from rest_framework.permissions import BasePermission, SAFE_METHODS

from . import constants, models

class IsSupplier(BasePermission):
    def has_permission(self, request, view):
        role = None
        user = request.user
        if not user.is_anonymous:
            user_profile = models.GrainsUserProfile.objects.filter(user__email=user.email).first()
            if user_profile:
                role = user_profile.role
        if request.method in SAFE_METHODS:
            return True
        return bool(user.is_authenticated and role == constants.SUPPLIER)
