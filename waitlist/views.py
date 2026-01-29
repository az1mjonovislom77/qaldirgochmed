from datetime import datetime
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet

from utils.base.views_base import BaseUserViewSet
from waitlist.models import WaitList
from waitlist.serializers import WaitListSerializer


@extend_schema(tags=['WaitList'])
class WaitListViewSet(BaseUserViewSet):
    queryset = WaitList.objects.all()
    serializer_class = WaitListSerializer


@extend_schema(tags=['WaitList'])
class DailyWaitListAPIView(ListCreateAPIView):
    serializer_class = WaitListSerializer

    def get_queryset(self):
        today = datetime.now().date()
        return WaitList.objects.filter(date__date=today).order_by('-date')
