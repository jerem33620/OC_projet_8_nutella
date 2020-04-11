# OC_projet_8_nutella

## Créez une plateforme pour amateurs de Nutella

La startup Pur Beurre, avec laquelle vous avez déjà travaillé, souhaite développer une plateforme web à destination de ses clients. Ce site permettra à quiconque de trouver un substitut sain à un aliment considéré comme "Trop gras, trop sucré, trop salé" (même si nous savons tous que le gras c’est la vie).


## Liens:

- Lien Trello: https://trello.com/b/GmCK4Nbb/projet8
- Lien Github: https://github.com/jerem33620/OC_projet_8_nutella
- Adresse URL: https://jeremy-p8.herokuapp.com/


## Fonctionnalités:

- Affichage du champ de recherche dès la page d’accueil
- La recherche ne doit pas s’effectuer en AJAX
- Interface responsive
- Authentification de l’utilisateur : création de compte en entrant un mail et un mot de passe, sans possibilité de changer son mot de passe pour le moment.


## Livrables:

- Lien vers votre site en production, entièrement fonctionnel.
- Document écrit expliquant votre démarche de création, les difficultés rencontrées et la manière dont vous les avez résolues. Incluez-y le lien vers votre board Trello ou Pivotal Tracker, le lien vers votre repo Github et le site en production.  Le document doit être en format pdf et ne pas excéder 2 pages A4. Il peut être rédigé en anglais ou en français, au choix, mais prenez bien en considération que les fautes d’orthographe et de grammaire seront évaluées !


## Contraintes:

- Tests : testez votre projet en adoptant la démarche qui vous semble la plus appropriée (TDD ou tests écrits à la fin d’une fonctionnalité)
- Utilisez une base de données PostgreSql et non MySQL sous peine de ne pas pouvoir déployer votre application sur Heroku.
- Incluez une page “Mentions Légales” qui contiendra les coordonnées de l’hébergeur ainsi que les auteurs des différentes ressources libres utilisées (template, photos, icônes, …).
- Suivez les bonnes pratiques de la PEP 8
- Pushez votre code régulièrement sur Github et créez des PR quand vous souhaitez avoir le retour de votre mentor.
- Votre code doit être intégralement écrit en anglais : fonctions, commentaires, …
- Utilisez une méthodologie de projet agile pour travailler en mode projet.

### Installer:

Pour installer et faire fonctionner mon projet vous aurez besoin de certains packages et vous aurez besoin de clonner mon projet de github sur votre machine avec git:

```
- $ git clone https://github.com/jerem33620/OC_projet_8_nutella
```

Puis, pour les packages:

```
- $ python -m pip install pipenv
- $ python -m pipenv install requests django django-heroku gunicorn selenium coverage
```

## Tests:

Pour lancer votre tests vous devrez utiliser les lignes de code suivante:

```
- $ coverage run –source=’.’ manage.py test
- $ coverage report
```

ou sinon:

```
- $ python manage.py test
```

### Activer votre projet en local:

Il faudra lancer 2 commandes et vous aurez le projet d'activé.

```
- $ python -m pipenv shell

- $ python manage.py runserver
```