from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Delivery, Favorabledelivery

class DeliveryAdmin(TranslationAdmin):
    fieldsets = (
        ('Main Information', {
            'fields': ('title', 'descriptions', 'banner_image'),
        }),
        ('Trust Information', {
            'fields': ('trust_title', 'trust_descriptions', 'trust_descriptions2', 'trust_image'),
        }),
    )

class FavorabledeliveryAdmin(TranslationAdmin):
    list_display = ('title_base', 'title', 'descriptions')

admin.site.register(Delivery, DeliveryAdmin)
admin.site.register(Favorabledelivery, FavorabledeliveryAdmin)

