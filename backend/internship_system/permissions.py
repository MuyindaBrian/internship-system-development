from rest_framework import permissions


class IsAdmin(permissions.BasePermission):
    """
    Allows access only to admin users.
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.user_type == 'admin'


class IsStudent(permissions.BasePermission):
    """
    Allows access only to student users.
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.user_type == 'student'


class IsCompany(permissions.BasePermission):
    """
    Allows access only to company users.
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.user_type == 'company'


class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Allows admin users to edit, others get read-only access.
    """
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_authenticated and request.user.user_type == 'admin'


class IsAdminOrCompany(permissions.BasePermission):
    """
    Allows admin or company users to perform write actions.
    """
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_authenticated and request.user.user_type in ('admin', 'company')


class IsOwnerOrAdmin(permissions.BasePermission):
    """
    Allows owners or admin users to edit objects.
    """
    def has_object_permission(self, request, view, obj):
        if request.user and request.user.is_authenticated and request.user.user_type == 'admin':
            return True
        owner = (
            getattr(obj, 'requested_by', None) or
            getattr(obj, 'submitted_by', None) or
            getattr(obj, 'applicant', None)
        )
        return owner == request.user
