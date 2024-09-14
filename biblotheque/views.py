from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Livre, Emprunt, Emprunteur, Utilisateur
from django.contrib.auth import login
from django.contrib.auth.models import User

def liste_livres(request):
    query = request.GET.get('q', '')  # Récupère le terme de recherche depuis la requête GET
    if query:
        # Filtre les livres par titre ou auteur en fonction du terme de recherche
        livres = Livre.objects.filter(titre__icontains=query) | Livre.objects.filter(auteur__icontains=query)
    else:
        livres = Livre.objects.all()  # Affiche tous les livres si aucun terme de recherche n'est fourni
    
    return render(request, 'bibliotheque/index.html', {'livres': livres, 'query': query})

 
#etait prevu pour permettre a l'utilisateur d'emprunter  directement un livre sur l'interface
@login_required
def emprunter_livre(request, livre_id):
    # Récupérer l'utilisateur actuellement connecté
    utilisateur = request.user

    # Récupérer le livre à emprunter
    livre = get_object_or_404(Livre, id=livre_id)

    # Créer un nouvel emprunt
    emprunt = Emprunt.objects.create(utilisateur=utilisateur, livre=livre)

    # Rediriger l'utilisateur vers la page d'index
    return redirect('index')


 

def inscription(request):
    if request.method == 'POST':
        prenom = request.POST['prenom']
        username = request.POST['username']
        numero = request.POST['numero']
        email = request.POST['email']
        password = request.POST['password']

        # Vérification de l'existence de l'utilisateur
        if Utilisateur.objects.filter(username=username).exists():
            return render(request, 'bibliotheque/signup.html', {'error_message': 'Nom d\'utilisateur déjà pris.'})
        elif Utilisateur.objects.filter(email=email).exists():
            return render(request, 'bibliotheque/signup.html', {'error_message': 'Email déjà utilisé.'})
        else:
            # Création du nouvel utilisateur
            user = Utilisateur.objects.create_user(
                username=username,
                password=password,
                email=email,
                prenom=prenom,
                numero=numero
            )
            login(request, user)  # Connecte l'utilisateur après inscription
            return redirect('index')  # Redirige vers la page d'accueil après inscription

    return render(request, 'bibliotheque/signup.html')
