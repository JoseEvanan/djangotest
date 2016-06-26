from django.shortcuts import render
from .models import data
def index(request):
    datas = data.objects.all()
    return render(request,"start/home.html",{"data":datas})
def save(request):
    value = str(request.GET['value'])
    dat = data(value=value)
    dat.save()
    return render(request,"start/save.html")

def show(request):
    return render(request,"start/show.html")