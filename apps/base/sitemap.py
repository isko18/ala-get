from django.contrib.sitemaps import Sitemap
from apps.base.models import Settings, Slider, Why, Base, Environment
from apps.betaxist.models import Betaxist, EarnMoney
from apps.cargo.models import Cargo, Profitable
from apps.taxi.models import Taxi, TypesTaxi
from apps.contact.models import Contact
from apps.delivery.models import Delivery
from apps.partners.models import Partners, LocalTaxi, PartnersSlider, PartnersSlider2


class SettingsSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Settings.objects.all()
    
    def lastmod(self, obj):
        pass

class SliderSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Slider.objects.all()
    
    def lastmod(self, obj):
        pass

class WhySitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Why.objects.all()
    
    def lastmod(self, obj):
        pass


class BaseSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Base.objects.all()
    
    def lastmod(self, obj):
        pass


class EnvironmentSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Environment.objects.all()
    
    def lastmod(self, obj):
        pass


class BetaxistSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Betaxist.objects.all()
    
    def lastmod(self, obj):
        pass

class EarnMoneySitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return EarnMoney.objects.all()
    
    def lastmod(self, obj):
        pass

class CargoSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Cargo.objects.all()
    
    def lastmod(self, obj):
        pass


class TaxiSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Taxi.objects.all()
    
    def lastmod(self, obj):
        pass

class TypesTaxiSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return TypesTaxi.objects.all()
    
    def lastmod(self, obj):
        pass

class ContactSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Contact.objects.all()
    
    def lastmod(self, obj):
        pass


class DeliverySitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Delivery.objects.all()
    
    def lastmod(self, obj):
        pass

class PartnersSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Partners.objects.all()
    
    def lastmod(self, obj):
        pass

class LocalTaxiSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return LocalTaxi.objects.all()
    
    def lastmod(self, obj):
        pass

class PartnersSliderSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return PartnersSlider.objects.all()
    
    def lastmod(self, obj):
        pass

class PartnersSlider2Sitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return PartnersSlider2.objects.all()
    
    def lastmod(self, obj):
        pass