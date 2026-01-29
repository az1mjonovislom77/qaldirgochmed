from django.urls import path, include
from rest_framework.routers import DefaultRouter

from category.views import CategoryViewSet, PriceListViewSet, ConsultationViewSet

router = DefaultRouter()
router.register('category', CategoryViewSet)
router.register('pricelist', PriceListViewSet)
router.register('consultation', ConsultationViewSet)

urlpatterns = [
    path('', include(router.urls)),

]
