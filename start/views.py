from django.shortcuts import render
from .models import data
def index(request):
    print "llego a index"
    datas = data.objects.all()
    return render(request,"start/home.html",{"data":datas})
def save(request):
    #http://127.0.0.1:8000/save/?value=12
    value = str(request.GET['value'])
    dat = data(value=value)
    dat.save()
    return render(request,"start/save.html")