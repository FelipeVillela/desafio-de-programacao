from django.shortcuts import render
from .models  import SalesData
from django.http import HttpResponse

# Create your views here.
def hello_world(request, *args, **kwargs):

    return HttpResponse("Hello World")

