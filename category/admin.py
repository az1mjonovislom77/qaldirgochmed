from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from category.models import Category, PriceList, Consultation


@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    search_fields = ('name',)
    list_display = ('id', 'name', 'slug')


@admin.register(PriceList)
class PriceListAdmin(TranslationAdmin):
    list_display = ('id', 'title')


@admin.register(Consultation)
class ConsultationAdmin(TranslationAdmin):
    list_display = ('id', 'title')
