from django.shortcuts import render
from apps.betaxist.models import Betaxist, EarnMoney
from apps.base.models import Settings, Base, Environment


# Create your views here.
def betaxist(request):
    title = "Стать водителем"
    betaxist = Betaxist.objects.latest('id')
    settings = Settings.objects.latest('id')
    earnnoney = EarnMoney.objects.all()
    base = Base.objects.latest('id')
    environment = Environment.objects.latest('id')


    return render(request, 'beTaxist.html', locals())