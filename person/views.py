from django.shortcuts import render



# Create your views here.


from django.http import HttpResponse



def dummy(request):
    return HttpResponse("hello world")
    