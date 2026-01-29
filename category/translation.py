from modeltranslation.translator import register, TranslationOptions

from .models import Category, PriceList, Consultation


@register(Category)
class CategoryTranslation(TranslationOptions):
    fields = ('name',)


@register(PriceList)
class PriceListTranslation(TranslationOptions):
    fields = ('title',)


@register(Consultation)
class ConsultationTranslation(TranslationOptions):
    fields = ('title',)
