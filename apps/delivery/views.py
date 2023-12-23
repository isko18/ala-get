from django.shortcuts import render
from apps.delivery.models import Delivery, Favorabledelivery
from apps.cargo.models import  Profitable
from apps.base.models import Settings, OrderIntercity, Why, Earn, Base
from apps.taxi.models import Taxi, TypesTaxi
# Create your views here.
def delivery(request):
    title = "Доставка"
    delivery = Delivery.objects.latest('id')
    settings = Settings.objects.latest('id')
    profitable = Profitable.objects.all()
    typestaxi = TypesTaxi.objects.all()
    taxi = Taxi.objects.latest('id')
    orderintercity = OrderIntercity.objects.all()
    whys = Why.objects.latest('id')
    why = Why.objects.all().order_by('?')[:3]
    earn = Earn.objects.latest('id')
    base = Base.objects.latest('id')
    favorabledelivery = Favorabledelivery.objects.all()[:3]
    favorabledeliverys = Favorabledelivery.objects.latest('id')


    return render(request, 'delivery.html', locals())