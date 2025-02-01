from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse



def dummy(request):
    data = [{
        "name": "Satkhira Polytechnic Institue",
        "location": "Satkhira"
    }]
    return HttpResponse(data)
    