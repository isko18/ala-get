from django.contrib import admin
from apps.about.models import About, OurMission
from modeltranslation.admin import TranslationAdmin
# Register your models here.

class AboutAdmin(TranslationAdmin):
    list_display = ('our_mission', 'mission_descriptions', 'vision', 'vision_descriptions')

class OurMissionAdmin(TranslationAdmin):
    list_display = ('title', 'descriptions', 'descriptions2', 'numbers')

admin.site.register(About,AboutAdmin)
admin.site.register(OurMission, OurMissionAdmin)

