from django.core.exceptions import PermissionDenied


class CartSessionRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        if "cart_id" not in request.session:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
