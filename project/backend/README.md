# Backend de l'Application

L'application utilise Flask comme framework backend et Redis comme base de données pour le stockage des données.


## Structure du Backend

Le backend est organisé en plusieurs dossiers, chacun avec ses propres fonctionnalités :

- **auth**: Contient les routes et la logique pour l'authentification des utilisateurs.
  - **auth.py**: Gestion des routes d'authentification, telles que l'inscription, la connexion et la déconnexion.
- **redis_db**: Gère la connexion à la base de données Redis.
- **store**: Contient les classes et les méthodes pour la gestion des utilisateurs, des tweets et des sujets.
  - **topic.py**: Gestion des sujets.
  - **tweet.py**: Gestion des tweets.
  - **user.py**: Gestion des utilisateurs.
- **topic**: Fournit les routes pour la récupération des sujets.
- **tweet**: Fournit les routes pour la création et la récupération des tweets.



## Routes Principales

- **POST /tweets**: Permet de créer un nouveau tweet. Les données JSON doivent contenir les champs "email" (email de l'utilisateur) et "tweet" (contenu du tweet).
- **GET /tweets**: Récupère la liste de tous les tweets ou les tweets associés à un utilisateur spécifique ou à un sujet spécifique.
- **GET /topics**: Récupère la liste de tous les sujets (topics) disponibles.


## Technologies Utilisées

- Flask
- Redis
- Flask-CORS
