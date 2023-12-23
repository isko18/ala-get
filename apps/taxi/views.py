from django.shortcuts import render
from apps.taxi.models import Taxi, TypesTaxi
from apps.base.models import Settings, OrderСity, OrderIntercity, Why, Earn, Base
# Create your views here.
def taxi(request):
    title = "Такси"
    settings = Settings.objects.latest('id')
    taxi = Taxi.objects.latest('id')
    typestaxi = TypesTaxi.objects.latest('id')
    ordercity = OrderСity.objects.all()
    orderintercity = OrderIntercity.objects.all()
    why = Why.objects.all().order_by('?')[:3]
    whys = Why.objects.latest('id')

    earn = Earn.objects.latest('id')
    base = Base.objects.latest('id')

    return render(request, 'taxi.html', locals())
