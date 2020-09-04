from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, Http404
from django.shortcuts import render


def index(request):
    context = {'index': 'index'}
    return render(request, 'figma/index.html', context)

def base_list(request):
    return render(request, "figma/base_list.html", {'base_list': 'base_list'})