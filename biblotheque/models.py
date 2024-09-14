
# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser

# Modèle pour les utilisateurs
class Utilisateur(AbstractUser):
    prenom = models.CharField(max_length=50, verbose_name="Prénom")
    numero = models.CharField(max_length=15, unique=True, verbose_name="Numéro de téléphone")

    groups = models.ManyToManyField(
        'auth.Group',
       
        blank=True,
        
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        
        blank=True,
       
    )

    class Meta:
        verbose_name = "Utilisateur"
        

    def __str__(self):
        return f"{self.username} ({self.prenom})"

# Modèle pour les livres
from django.db.models import Count

class Livre(models.Model):
    titre = models.CharField(max_length=200, unique=True, verbose_name="Titre")
    auteur = models.CharField(max_length=100, verbose_name="Auteur")
    date_publication = models.DateField(verbose_name="Date de publication")
    nombre_total = models.IntegerField(default=1, verbose_name="Nombre total de copies")

    @property
    def nombre_disponible(self):
        emprunts_en_cours = Emprunt.objects.filter(livre=self, retourne=False).count()
        return self.nombre_total - emprunts_en_cours

    class Meta:
        verbose_name = "Livre"
        verbose_name_plural = "Livres"

    def __str__(self):
        return self.titre



# Modèle pour les emprunteurs
class Emprunteur(models.Model):
    utilisateur = models.OneToOneField(Utilisateur, on_delete=models.CASCADE, verbose_name="Utilisateur")
    numero_carte = models.CharField(max_length=20, unique=True, verbose_name="Numéro de carte")

    class Meta:
        verbose_name = "Emprunteur"
        verbose_name_plural = "Emprunteurs"

    def __str__(self):
        return self.utilisateur.username

# Modèle pour les emprunts
class Emprunt(models.Model):
    livre = models.ForeignKey(Livre, on_delete=models.CASCADE, verbose_name="Livre")
    emprunteur = models.ForeignKey(Emprunteur, on_delete=models.CASCADE, verbose_name="Emprunteur")
    date_emprunt = models.DateField(null=True,blank=True, verbose_name="Date d'emprunt")
    date_retour = models.DateField(null=True, blank=True, verbose_name="Date de retour")
    retourne = models.BooleanField(default=False, verbose_name="Retourné")

    class Meta:
        verbose_name = "Emprunt"
        verbose_name_plural = "Emprunts"

    def __str__(self):
        return f"{self.livre.titre} emprunté par {self.emprunteur.utilisateur.username}"
