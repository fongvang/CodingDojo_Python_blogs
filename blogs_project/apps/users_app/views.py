from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def register(request):
    return HttpResponse('placeholder for uers to create a new user')

def login(request):
    return HttpResponse('This is where users will log in to their accoutns!')

def new(request):
    return HttpResponse('Where users will create a new account')

def users(request):
    return HttpResponse('display all list of users')
