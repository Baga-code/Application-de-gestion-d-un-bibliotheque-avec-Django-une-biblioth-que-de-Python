# Projet de Gestion de Bibliothèque

## Prérequis

- Python 3.x
- Pip
- Virtualisation



==================commande a executer avant de lancer de projet==========================
// creer l'environnement virtuel

python -m venv evirtuel

// ajouter le dossier 'projet' dans evirtuel 

.\\scripts\activate  # avant naviguer jusqu'au dossier evirtuel d'abord

pip install -r requirements.txt

python manage.py runserver # pour demmarer le serveur 


#les commande utiliser 


python -m venv evirtuel  //(envirronnemnt virtuiel)

cd evirtuel // pour entrer dans le dossier virtuel

.\\scripts\activate //pour active l'environement virtuel

pip install django // pour installer la dernier version de django


pip freeze //pour voir les parkaer installer 

pip freeze > requirements.txt //(pour mettre les  dependance dans un fichier txt )

pip install -r requirements.txt //   pour installer les meme dependance du projet (obigatoire)

django-admin startproject projet //(pour créer le projet)



cd projet //(pour entrer dans le dossier )
python manage.py createsuperuser // pour creer le super admin pour la gestion d'admin
python manage.py startapp bibliotheque //(créer une application pour la biblotheque)

==================commande utiliser=====================================================

python -m venv evirtuel
cd 
pip install django
pip freeze 
pip install -r requirements.txt
django-admin startproject projet
python manage.py startapp bibliotheque
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
python manage.py createsuperuser


