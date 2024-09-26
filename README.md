# Livres
Site en Django voué à la gestion de sa bibliothèque et au suivi de ses lectures.

## Installation et lancement [LINUX]

Cloner le dépôt :
```sh
git clone https://github.com/closzach/Livres.git
```

### Méthode 1 - Docker
Pour pouvoir utiliser cette méthode d'installation il faut au préalable avoir docker et docker-compose sur sa machine hôte. Pour pouvoir installer docker-compose, merci de suivre les instructions sur la [documentation officielle](https://docs.docker.com/compose/)

Après être sûr d'avoir docker et docker-compose, lancer la commande suivante à la racine du projet (là où sont présents les fichiers Dockerfile et compose.yml) : 
```sh
docker compose up
```

Cela va créer un conteneur et une image et un conteneur docker l'exécuter.

Pour plus d'informations sur les conteneurs Docker et leur utilisation, se rendre sur la [documentation officielle](https://docs.docker.com/reference/cli/docker/container/)

### Méthode 2 - Sans Docker

Créer un environnement Python 3.12 et le lancer(facultatif) :
```sh
python3.12 -m pip venv my_env && source my_env/bin/activate
```

Installer les librairies :
```sh
python -m pip install -r requirements.txt
```

Lancer le serveur :
```sh
python ./Livres/manage.py runserver
```

Après avoir fait l'installation et lancé avec une des méthodes, accèder au site avec l'url suivante :

```
http://127.0.0.1:8000/
```