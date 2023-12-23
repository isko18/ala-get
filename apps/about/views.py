from django.shortcuts import render
from apps.about.models import About, OurMission
from apps.base.models import Settings, Earn, Base


# Create your views here.
def about(request):
    title = "О нас"
    about = About.objects.latest('id')
    settings = Settings.objects.latest('id')
    ourmission = OurMission.objects.all()
    earn = Earn.objects.latest('id')
    base = Base.objects.latest('id')

    return render(request, 'about.html', locals())