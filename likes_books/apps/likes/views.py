from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
def index(request):

  return HttpResponse("This is Likes/Books")