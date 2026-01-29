from django.urls import path, include
from .views import DailyWaitListAPIView, WaitListViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('waitlist', WaitListViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('daily_waitlist/', DailyWaitListAPIView.as_view(), name='daily-wait-list'),
]
