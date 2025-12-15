from django.urls import path
from . import views

urlpatterns = [
    path("allegebruikers", views.allegebruikers),
    path("eengebruiker/<int:id>", views.toon1Gebruiker),
    path("maakgebruiker", views.maakgebruiker),
    path("wisgebruiker", views.wisGebruiker),
    path("editgebruiker/<int:id>", views.pasGebruikerAan),
    path("controlgebruiker/<int:id>", views.controleerGebruiker)
]