from modeltranslation.translator import register, TranslationOptions
from .models import Doctor


@register(Doctor)
class DoctorTranslation(TranslationOptions):
    fields = ('full_name', 'profession', 'education', 'works')
