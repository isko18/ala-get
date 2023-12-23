from modeltranslation.translator import register, TranslationOptions


from apps.about.models import About, OurMission

@register(About)
class AboutTranslationOptions(TranslationOptions):
    fields = ('our_mission', 'mission_descriptions', 'vision', 'vision_descriptions')

@register(OurMission)

class OurMissionTranslationOptions(TranslationOptions):
    fields = ('title', 'descriptions', 'descriptions2', 'numbers')



