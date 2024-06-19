from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#an endpoint is the thing after slash\

def main(request):
     return HttpResponse("Hello")