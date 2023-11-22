from django.shortcuts import render
from .models import place
from .models import Team

from django.http import HttpResponse
# Create your views here.
def demo(request):
    obj=place.objects.all()
    return render(request,'index.html',{'result':obj})
def fun(request):
    obj2=Team.objects.all()
    return render(request,'index.html',{'output':obj2})