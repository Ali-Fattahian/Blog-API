from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsAllowedToCreatePost(BasePermission):
    """Checks if the user is a trusted user"""
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user.groups.filter(name='trusted_users').exists()


class IsAllowedToChangePost(BasePermission):
    """Only allows author of the object to change or delete it"""
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        else:
            return obj.author == request.user
