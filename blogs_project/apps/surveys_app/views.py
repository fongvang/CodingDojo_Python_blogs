from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def index(request):
    return HttpResponse('placeholder page for later surveys')

def new(request):
    return HttpResponse('survey new form!')
