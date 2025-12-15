from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import gebruikers
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict

# Create your views here.

def allegebruikers(request):
    alleUsers = gebruikers.objects.all().values()
    print(alleUsers)
    returnAll = list(alleUsers)
    return JsonResponse(returnAll, safe=False)

def toon1Gebruiker(request, id):
    gebruikers.objects.get(pk == id)
    return HttpResponse()

@csrf_exempt
def maakgebruiker(request):
    return HttpResponse("gelukt")

@csrf_exempt
def wisGebruiker(request):
    return JsonResponse()

@csrf_exempt
def pasGebruikerAan(request):
    return JsonResponse()

@csrf_exempt
def controleerGebruiker(request):
    return JsonResponse()