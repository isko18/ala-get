from django.shortcuts import render, get_object_or_404
from apps.base.models import Settings, Slider, Why, Base, Environment

# Create your views here.
def settings(request):
    title = "Главная"
    settings = Settings.objects.latest('id')
    slider = Slider.objects.all()
    why = Why.objects.all().order_by('?')[:3]
    whys = Why.objects.latest('id')
    base = Base.objects.latest('id')
    environment = Environment.objects.latest('id')


    return render(request, 'index.html', locals())


def politikConfidital(request):
    title = "Политика конфиденциальности"
    settings = Settings.objects.latest('id')
    slider = Slider.objects.all()
    why = Why.objects.all().order_by('?')[:3]
    whys = Why.objects.latest('id')
    base = Base.objects.latest('id')
    environment = Environment.objects.latest('id')


    return render(request, 'politikConfidital.html', locals())


def soglashenie(request):
    title = "Пользовательское соглашение"
    settings = Settings.objects.latest('id')
    slider = Slider.objects.all()
    why = Why.objects.all().order_by('?')[:3]
    whys = Why.objects.latest('id')
    base = Base.objects.latest('id')
    environment = Environment.objects.latest('id')
    return render(request, 'soglashenie.html', locals())



def LicenseAgreement(request):
    title = "Лицензионное соглашение"
    settings = Settings.objects.latest('id')
    slider = Slider.objects.all()
    why = Why.objects.all().order_by('?')[:3]
    whys = Why.objects.latest('id')
    base = Base.objects.latest('id')
    environment = Environment.objects.latest('id')
    return render(request, 'LicenseAgreement.html', locals())



def errors(request, exception):
    return render(request, "404/404.html", status=404)