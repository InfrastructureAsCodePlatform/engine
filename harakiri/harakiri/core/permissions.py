from rest_framework.permissions import BasePermission


class IsObjectOwner(BasePermission):
    def has_permission(self, request, view):
        if request.method in ["POST", "PUT"]:
            if "user" not in request.data or request.user.id != request.data["user"]:
                return False
        return True

    def has_object_permission(self, request, view, obj):
        return request.user == obj.user
