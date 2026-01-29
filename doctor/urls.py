from django.urls import path, include
from rest_framework.routers import DefaultRouter
from doctor.views import DoctorViewSet, StickersViewSet

router = DefaultRouter()
router.register('doctor', DoctorViewSet)
router.register('stickers', StickersViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
