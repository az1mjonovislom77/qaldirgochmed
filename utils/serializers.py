from rest_framework import serializers

from utils.models import HomepageStats, SocialMedia, Location, AboutClinic, FooterImage, FooterPage, Terapy, TypeTerapy


class HomePageStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomepageStats
        fields = '__all__'


class SocialMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMedia
        fields = '__all__'


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'


class AboutClinicSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutClinic
        fields = '__all__'


class AllUtilsGetSerializer(serializers.Serializer):
    home_page_stats = HomePageStatsSerializer(many=True)
    social_media = SocialMediaSerializer(many=True)
    location = LocationSerializer(many=True)
    about_clinic = AboutClinicSerializer(many=True)


class FooterImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = FooterImage
        fields = '__all__'


class FooterPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = FooterPage
        fields = '__all__'


class TerapySerializer(serializers.ModelSerializer):
    class Meta:
        model = Terapy
        fields = '__all__'


class TypeTerapySerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeTerapy
        fields = '__all__'
