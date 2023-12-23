from django.contrib import admin
from apps.base.models import Settings, Slider, Why, OrderСity, OrderIntercity, Earn, Base, Environment
from modeltranslation.admin import TranslationAdmin
# Register your models here.

class SettingsAdmin(TranslationAdmin):
    list_display = ('title', 'title2', 'descriptions', 'advantage1', 'advantage2', 'advantage3', 'made_title', 'made_descriptions', 'install')

class SliderAdmin(TranslationAdmin):
    list_display = ('title_slider', 'numbering', 'descriptions', 'title_slider2')

class WhyAdmin(TranslationAdmin):
    list_display = ('why', 'title', 'descriptions')

class OrderСityAdmin(TranslationAdmin):
    list_display = ('title', 'numbers', 'descriptions')

class OrderIntercityAdmin(TranslationAdmin):
    list_display = ('title', 'numbers', 'descriptions')

class EarnAdmin(TranslationAdmin):
    list_display = ('title', 'descriptions')


class BaseAdmin(TranslationAdmin):
    list_display = (
        'title1', 'title2', 'title3', 'title4',
        'title5', 'title6', 'title7', 'title8',
        'title9', 'descriptions'
    )
class EnvironmentAdmin(TranslationAdmin):
    list_display = ('title', 'descriptions', 'descriptions2', 'descriptions3')

admin.site.register(Settings, SettingsAdmin)
admin.site.register(Slider, SliderAdmin)
admin.site.register(Why, WhyAdmin)
admin.site.register(OrderСity, OrderСityAdmin)
admin.site.register(OrderIntercity, OrderIntercityAdmin)
admin.site.register(Earn, EarnAdmin)
admin.site.register(Base, BaseAdmin)
admin.site.register(Environment,EnvironmentAdmin)





