from modeltranslation.translator import register, TranslationOptions
from .models import Doctor


@register(Doctor)
class DoctorTranslation(TranslationOptions):
    fields = ('full_name', 'profession', 'institution', 'specialties', 'education', 'works', 'services', 'achievements',
              'full_bio')
