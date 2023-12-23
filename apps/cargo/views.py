from django.shortcuts import render
from apps.cargo.models import Cargo, Profitable
from apps.taxi.models import Taxi, TypesTaxi
from apps.base.models import Settings,OrderIntercity, Earn, Why, Base
# Create your views here.
def cargo(request):
    title = "Грузоперевозки"
    cargo = Cargo.objects.latest('id')
    profitable = Profitable.objects.all()
    settings = Settings.objects.latest('id')
    profitables = Profitable.objects.latest('id')
    typestaxi = TypesTaxi.objects.all()
    orderintercity = OrderIntercity.objects.all()
    earn = Earn.objects.latest('id')
    whys = Why.objects.latest('id')
    why = Why.objects.all().order_by('?')[:3]
    base = Base.objects.latest('id')

    return render(request, 'cargo.html', locals())