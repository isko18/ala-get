from django.shortcuts import render
from apps.partners.models import Partners, LocalTaxi, PartnersSlider, PartnersSlider2
from apps.base.models import Settings, Base
from apps.contact.models import Contact

# Create your views here.
def partners(request):
    title = "Партнерство"
    partners = Partners.objects.latest('id')
    localtaxi = LocalTaxi.objects.all()
    settings = Settings.objects.latest('id')
    base = Base.objects.latest('id')
    partnersslider = PartnersSlider.objects.all()
    partnersslider2 = PartnersSlider2.objects.all()

    contact = Contact.objects.latest('id')


    return render(request, 'partners.html', locals())