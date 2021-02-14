from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from app.models import Animals
# Create your views here.

def index(request):
    total = len(Animals.objects.all())
    context = {'total' : total}
    return render(request,'index.html',context)