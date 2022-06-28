from django.db import models

class Projet(models.Model):
    nom_du_produit=models.CharField(max_length=50)
    description=models.TextField()
    prix_TTC=models.IntegerField(null=True)
    image_url=models.CharField(max_length=2000)
