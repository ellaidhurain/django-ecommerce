from django.core.exceptions import PermissionDenied


# mixin for class based view
class GroupPermissionMixin:
    def dispath(self, request, *args, **kwargs ):
        if request.user.groups.filter(name= 'customer').exists():
        
            return super().dispatch(request, *args, **kwargs)
            
        else:
            raise PermissionDenied