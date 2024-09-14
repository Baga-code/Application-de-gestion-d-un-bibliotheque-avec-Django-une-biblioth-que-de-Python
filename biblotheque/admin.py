from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Utilisateur, Livre, Emprunteur, Emprunt

# Enregistrement des modèles dans l'admin
admin.site.register(Utilisateur)
admin.site.register(Livre)
admin.site.register(Emprunteur)
admin.site.register(Emprunt)
