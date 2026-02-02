from django.urls import path, include
from .views import HomePageStatsViewSet, SocialMediaViewSet, LocationViewSet, AboutClinicViewSet, FooterImageViewSet, \
    FooterPageViewSet, TerapyViewSet, TypeTerapyViewSet, AllUtilsGetAPIView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('homepage-stats', HomePageStatsViewSet)
router.register('social-media', SocialMediaViewSet)
router.register('location', LocationViewSet)
router.register('aboutclinic', AboutClinicViewSet)
router.register('footerimage', FooterImageViewSet)
router.register('footerpage', FooterPageViewSet)
router.register('terapy', TerapyViewSet)
router.register('typeterapy', TypeTerapyViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('all_utils/', AllUtilsGetAPIView.as_view())
]
