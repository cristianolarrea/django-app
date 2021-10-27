from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("<strong>FGV</strong>")

def special(request):
    return render(request, 'fgv/fgv.html')