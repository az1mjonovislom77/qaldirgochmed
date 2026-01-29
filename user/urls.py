from django.urls import path, include
from rest_framework.routers import DefaultRouter
from user.views.auth_views import SignInAPIView, LogOutAPIView
from user.views.user_views import UserViewSet, MeAPIView

router = DefaultRouter()
router.register('user', UserViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path("login/", SignInAPIView.as_view()),
    path("logout/", LogOutAPIView.as_view()),
    path("me/", MeAPIView.as_view())
]
