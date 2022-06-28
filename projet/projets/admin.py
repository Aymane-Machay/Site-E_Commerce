from django.contrib import admin
from .models import Projet


class ProjetAdmin(admin.ModelAdmin):
    list_display = ('nom_du_produit', 'description', 'prix_TTC')

admin.site.register(Projet, ProjetAdmin)
