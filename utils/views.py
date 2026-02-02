from drf_spectacular.utils import extend_schema
from rest_framework.response import Response
from rest_framework.views import APIView

from utils.base.views_base import BaseUserViewSet
from utils.models import HomepageStats, SocialMedia, Location, AboutClinic, FooterImage, FooterPage, Terapy, TypeTerapy
from utils.serializers import HomePageStatsSerializer, SocialMediaSerializer, LocationSerializer, \
    AboutClinicSerializer, FooterImageSerializer, FooterPageSerializer, TerapySerializer, TypeTerapySerializer, \
    AllUtilsGetSerializer


@extend_schema(tags=["HomepageStats"])
class HomePageStatsViewSet(BaseUserViewSet):
    queryset = HomepageStats.objects.all()
    serializer_class = HomePageStatsSerializer


@extend_schema(tags=['SocialMedia'])
class SocialMediaViewSet(BaseUserViewSet):
    queryset = SocialMedia.objects.all()
    serializer_class = SocialMediaSerializer


@extend_schema(tags=['Location'])
class LocationViewSet(BaseUserViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


@extend_schema(tags=['AboutClinic'])
class AboutClinicViewSet(BaseUserViewSet):
    queryset = AboutClinic.objects.all()
    serializer_class = AboutClinicSerializer


@extend_schema(tags=['FooterImage'])
class FooterImageViewSet(BaseUserViewSet):
    queryset = FooterImage.objects.all()
    serializer_class = FooterImageSerializer


@extend_schema(tags=['Footer'])
class FooterPageViewSet(BaseUserViewSet):
    queryset = FooterPage.objects.all()
    serializer_class = FooterPageSerializer


@extend_schema(tags=['Terapy'])
class TerapyViewSet(BaseUserViewSet):
    queryset = Terapy.objects.all()
    serializer_class = TerapySerializer


@extend_schema(tags=['TypeTerapy'])
class TypeTerapyViewSet(BaseUserViewSet):
    queryset = TypeTerapy.objects.all()
    serializer_class = TypeTerapySerializer

@extend_schema(tags=["AllUtils"])
class AllUtilsGetAPIView(APIView):
    def get(self, request):
        data = {
            "home_page_stats": HomepageStats.objects.all(),
            "social_media": SocialMedia.objects.all(),
            "location": Location.objects.all(),
            "about_clinic": AboutClinic.objects.all(),
        }

        serializer = AllUtilsGetSerializer(data)
        return Response(serializer.data)
