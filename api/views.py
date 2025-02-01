from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse



def person(request):
    data ={
        "name": "Morsalin Islam",
        "profession": "backend developer"
    }

    return JsonResponse(data)
