# Create your views here.
from django.shortcuts import render, HttpResponse, redirect

def index(request):
  response = "Placeholder to later display all the list of blogs"
  return HttpResponse(response)

def new(request):
  response = "Placeholder to display a new form to create a new blog"
  return HttpResponse(response)

def create(request):
  return redirect("/")

def show(response, num):
  response = "placeholder to display blog " + num
  return HttpResponse(response)

def edit(response, num):
  response = "holder to edit blog " + num
  return HttpResponse(response)

def destroy(response, num):
  response = "placeholder to delete/destroy blog " + num
  return HttpResponse(response)
