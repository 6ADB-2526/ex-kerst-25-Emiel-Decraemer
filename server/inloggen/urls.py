from django.urls import path
from . import views

urlpatterns = [
    path("allegebruikers", views.allegebruikers),
    path("eengebruiker", views.toon1Gebruiker),
    path("maakgebruiker", views.maakgebruiker),
    path("wisgebruiker", views.wisGebruiker),
    path("editgebruiker", views.pasGebruikerAan),
    path("controlgebruiker", views.controleerGebruiker)
]