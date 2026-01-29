from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import Location, SocialMedia, HomepageStats, AboutClinic, FooterImage, FooterPage, Terapy, TypeTerapy


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('id', 'country', 'region')


@admin.register(SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'link')


@admin.register(HomepageStats)
class HomepageStatsAdmin(admin.ModelAdmin):
    list_display = ('id', 'happy_patients')


@admin.register(AboutClinic)
class AboutClinicAdmin(admin.ModelAdmin):
    list_display = ('id', 'number')


@admin.register(FooterImage)
class FooterImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'image')


@admin.register(FooterPage)
class FooterPageAdmin(TranslationAdmin):
    list_display = ('id', 'title')


@admin.register(Terapy)
class TerapyAdmin(TranslationAdmin):
    list_display = ('id', 'title')


@admin.register(TypeTerapy)
class TypeTerapyAdmin(TranslationAdmin):
    list_display = ('id', 'title')
