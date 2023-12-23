from modeltranslation.translator import register, TranslationOptions
from .models import Contact

@register(Contact)
class ContactTranslationOptions(TranslationOptions):
    fields = ('descriptions','firstname', 'name_company', 'number_email', 'title_form', 'title', 'title2')
