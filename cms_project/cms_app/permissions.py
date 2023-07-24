from rest_framework.permissions import BasePermission
from .models import User

class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        user= request.user._wrapped if hasattr(request.user,'_wrapped') else request.user
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD, or OPTIONS requests.
        if request.method in ['GET', 'HEAD', 'OPTIONS']:

            return True

        # Write permissions are only allowed to the owner of the blog.
        return obj.owner == user