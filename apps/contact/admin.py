from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Contact

class ContactAdmin(TranslationAdmin):
    list_display = ('descriptions','firstname', 'name_company', 'number_email', 'title_form', 'title', 'title2')


admin.site.register(Contact, ContactAdmin)
