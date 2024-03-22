# <div align="center"> Back-end </div>
<div align="center"> Le backend de Saison électorale 🌚 </div>

## TL;DR : Juste lancer le projet 🌤️
``` bash
docker compose up
```

Le back sera accessible à l'adresse suivante: http://localhost:8000

--- 

## Initialisation 🚀
Pour lancer l'environnement virtuel:
```bash
source .venv/bin/activate
```
Pour initialiser la data:
```bash
python3 seed.py
```
Cela ajoute (pour le moment) une partie des données seulement, à des fins de test. 



## DB 🫙
La base de données retenue est de type `postgresql`. Afin de visualiser la BDD, on utilisera:

```bash
prisma studio # cette commande ouvre localhost:5555, avec l'interface graphique Prisma de la BDD
```


## API

### Communes : toutes les communes 🏫
Pour avoir la liste de toutes les communes et leur data : 
- `commune/all`

### Communes : résultats élections ✉️

Pour avoir le résultat d'une élection, deux possibilités : 
- `commune/[code]/election/[electionType]/[tour]`: avec `code` le code commune de la commune, `electionType` LEG ou PRES ou EURO... (type de scrutin) et `tour` 1 ou 2 selon le tour (ce sera toujours 1 pour les européennes)
- `commune/[code]/election/[date]` avec la date au format `Y-m-j` (année mois jour, par ex. 2022-12-08)

Dans les deux cas, le résultat sera le même.

### Communes : météo ☁️
Pour avoir la météo d'un jour dans la commune :
- `/[code]/meteo/[date]` avec `code` le code commune de la commune et `date` la date au format `Y-m-j` (année mois jour).

### Communes : recherche 🔎
Pour rechercher les communes qui commencent par un texte : 
- `/commune/search?query=[txt]` avec `txt` la recherche de l'utilisateur

### Compare : comparaison générale 📊
Pour avoir à la fois la météo et l'abstention de toutes les communes : 
- `/compare/all/[date]` avec `date` la date au format Y-m-J

---

### Reste à faire : 🍱
TODO : /compare/all/[commune] : récupérer tous les résultats de la commune et sa météo
