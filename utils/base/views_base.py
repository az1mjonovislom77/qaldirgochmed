from rest_framework import viewsets


class PartialPutMixin:
    def update(self, request, *args, **kwargs):
        kwargs["partial"] = True
        return super().update(request, *args, **kwargs)


class BaseUserViewSet(PartialPutMixin, viewsets.ModelViewSet):
    http_method_names = ["get", "post", "put", "delete"]
