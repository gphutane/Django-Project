from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def ghar(request):
    return HttpResponse('<h1>Welcome to our ghar!!</h1>')