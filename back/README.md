# Backend
Le backend de Saison-electorale

## Initialisation 🚀
Pour lancer l'environnement virtuel:
```bash
source .venv/bin/activate
```
Pour monter la database:
````bash
cd db
docker compose up
````
Ensuite, pour initialiser la data:
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

### Communes : résultats élections ✉️

Pour avoir le résultat d'une élection, deux possibilités : 
- `/[code]/election/[electionType]/|tour]`: avec `code` le code commune de la commune, `electionType` LEG ou PRES ou EURO... (type de scrutin) et `tour` 1 ou 2 selon le tour (ce sera toujours 1 pour les européennes)
- `/[code]/election/[date]` avec la date au format `Y-m-j` (année mois jour, par ex. 2022-12-08)

Dans les deux cas, le résultat sera le même.

### Communes : météo ☁️
Pour avoir la météo d'un jour dans la commune :
- `/[code]/meteo/[date]` avec `code` le code commune de la commune et `date` la date au format `Y-m-j` (année mois jour).

