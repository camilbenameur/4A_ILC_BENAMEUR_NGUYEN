# Projet

Ce projet est composé de deux parties : frontend et backend.

## Frontend

Le frontend est développé avec [Vite](https://vitejs.dev/), un outil de développement rapide pour les applications web modernes en React.

### Installation des dépendances

```bash
cd project/frontend
npm install
```

### Construction de l'image Docker

```bash
cd project/frontend
docker build -t frontend-vite-server .
```

## Backend

Le backend est développé avec Flask.

### Construction de l'image Docker

```bash
cd backend
docker build -t flask-server .
```

## Project

Ce répertoire contient des configurations pour exécuter le projet à l'aide de Docker Compose.

### Exécution du projet avec Docker Compose

```bash
docker-compose up
```

### Forward le port 3000

Dans votre IDE il faut forward le port 127.0.0.1:3000.

Après avoir démarré les conteneurs Docker, vous pouvez accéder à l'expérience à l'URL suivante :

[http://localhost:5173/signin](http://localhost:5173/signin)
