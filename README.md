# Livres
Site en Django voué à la gestion de sa bibliothèque et au suivi de ses lectures.

## Installation et lancement [LINUX]

Cloner le dépôt :
```sh
git clone https://github.com/closzach/Livres.git
```

Créer un environnement Python 3.12 et le lancer(facultatif) :
```sh
python3.12 -m pip venv my_env && source my_env/bin/activate
```

Installer les librairies :
```sh
python -m pip install -r requirements.txt
```

Faire les migrations de la base de données
```sh
python python ./Livres/manage.py makemigrations && python ./Livres/manage.py migrate
```

Lancer le serveur :
```sh
python ./Livres/manage.py runserver
```

Après avoir fait l'installation et lancé avec une des méthodes, accèder au site avec l'url suivante :

```
http://127.0.0.1:8000/
```

## Documentation d'API

### Swagger
```
http://127.0.0.1:8000/swagger/
```

### Swagger JSON
```
http://127.0.0.1:8000/swagger.json/
```

### Swagger YAML
```
http://127.0.0.1:8000/swagger.yaml/
```

### Redoc
```
http://127.0.0.1:8000/redoc/
```
