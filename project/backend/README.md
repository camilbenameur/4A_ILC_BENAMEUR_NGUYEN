# Backend de l'Application

L'application utilise Flask comme framework backend et Redis comme base de données pour le stockage des données.


## Structure du Backend

Le backend est organisé en plusieurs dossiers, chacun avec ses propres fonctionnalités :

- **redis_db**: Gère la connexion à la base de données Redis.
- **store**: Contient les classes et les méthodes pour la gestion des utilisateurs, des tweets et des sujets.
  - **topic.py**: Gestion des sujets.
  - **tweet.py**: Gestion des tweets.
  - **user.py**: Gestion des utilisateurs.
- **auth**: Fournit les routes et la logique pour l'authentification des utilisateurs.
- **topic**: Fournit les routes pour la récupération des sujets.
- **tweet**: Fournit les routes pour la création et la récupération des tweets.

L'utilisation de blueprints nous permet d'avoir une api plus modulable.
L'utilisation du factory permet de déclaret plusieurs instances de l'application flask afin d'y charger différentes configurations de test ou autre.
L'utilisation d'un store permet d'isoler toutes manipulations de la base de données du reste de la logique de nos routes.

## Routes Principales

- **POST /tweets**: Permet de créer un nouveau tweet. Les données JSON doivent contenir les champs "email" (email de l'utilisateur) et "tweet" (contenu du tweet).
- **GET /tweets**: Récupère la liste de tous les tweets ou les tweets associés à un utilisateur spécifique ou à un sujet spécifique.
- **GET /topics**: Récupère la liste de tous les sujets (topics) disponibles.


## Technologies Utilisées

- Flask
- Redis
- Flask-CORS
