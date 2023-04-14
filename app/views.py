from django.shortcuts import render
from app.models import *
from django.db.models.functions import Length
from django.db.models import Q


# Create your views here.
def dis_webpage(request):
    wo=Webpage.objects.all()
    d={'web':wo}
    return render(request,'dis_webpage.html',context=d)
def page(request):
    low=Webpage.objects.all()
    low=Webpage.objects.filter(name='vinay')
    low=Webpage.objects.exclude(name='vinay')
    low=Webpage.objects.all()[1:4:]
    low=Webpage.objects.all().order_by('name')
    low=Webpage.objects.all().order_by('-name')
    low=Webpage.objects.filter(name__startswith='s')
    low=Webpage.objects.filter(name__endswith='h')
    low=Webpage.objects.filter(url__endswith='.com')
    low=Webpage.objects.filter(name__in=('vinay','srikanth'))


    d={'wob':low}
    return render(request,'page.html',d)
