from modeltranslation.translator import register, TranslationOptions

from utils.models import FooterPage, Terapy, TypeTerapy


@register(FooterPage)
class FooterPageTranslation(TranslationOptions):
    fields = ('title', 'description', 'works')


@register(Terapy)
class TerapyTranslation(TranslationOptions):
    fields = ('title', 'description', 'advantages')


@register(TypeTerapy)
class TerapyTranslation(TranslationOptions):
    fields = ('title', 'types')
