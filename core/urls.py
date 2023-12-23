"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import handler404
from django.conf.urls.i18n import i18n_patterns
from django.views.generic import TemplateView
from django.contrib.sitemaps.views import sitemap

from apps.base.sitemap import SettingsSitemap, SliderSitemap, WhySitemap, BaseSitemap,EnvironmentSitemap, BetaxistSitemap,EarnMoneySitemap, CargoSitemap, TaxiSitemap, TypesTaxiSitemap,ContactSitemap, DeliverySitemap, PartnersSitemap, LocalTaxiSitemap, PartnersSliderSitemap, PartnersSlider2Sitemap

sitemaps = {
    'settings' : SettingsSitemap,
    'slider' : SliderSitemap,
    'environment' : EnvironmentSitemap,
    'why' : WhySitemap,
    'base' : BaseSitemap,
    'environment': EnvironmentSitemap,
    'betaxist': BetaxistSitemap,
    'earnmoney': EarnMoneySitemap,
    'cargo': CargoSitemap,
    'taxi': TaxiSitemap,
    'typestaxi': TypesTaxiSitemap,
    'contact': ContactSitemap,
    'delivery': DeliverySitemap,
    'partners': PartnersSitemap,
    'localtaxi': LocalTaxiSitemap,
    'partnersslider': PartnersSliderSitemap,
    'partnersslider2': PartnersSlider2Sitemap,

}


urlpatterns = [
    path('admin/', admin.site.urls),
]

handler404 = 'apps.base.views.errors'

urlpatterns += i18n_patterns(
    #apps
    path('', include("apps.base.urls")),
    path('', include("apps.taxi.urls")),
    path('', include("apps.cargo.urls")),
    path('', include("apps.delivery.urls")),
    path('', include("apps.about.urls")),
    path('', include("apps.contact.urls")),
    path('', include("apps.betaxist.urls")),
    path('', include("apps.partners.urls")),
    
    #robots
    re_path('robots.txt', TemplateView.as_view(template_name = "robots.txt", content_type = "text/pali")),

    #sitemap
    re_path('sitemap.xml', sitemap, {'sitemaps' : sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
)



urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
