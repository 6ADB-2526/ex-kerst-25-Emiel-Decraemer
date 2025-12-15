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
    # een get werkt op pk - dus dit is niet nodig > gebruikers.id == id <
    gebruiker = gebruikers.objects.get(gebruikers.id == id)
    return JsonResponse(model_to_dict(gebruiker))

# Onderstaande functies hebben geen return of functionaliteit. 
# is dit te wijten aan te weinig studie? 

@csrf_exempt
def maakgebruiker(request):
    
    return HttpResponse("gelukt")

@csrf_exempt
def wisGebruiker(request):
    return JsonResponse()

@csrf_exempt
def pasGebruikerAan(request, id):
    return JsonResponse()

@csrf_exempt
def controleerGebruiker(request, id):
    return JsonResponse()