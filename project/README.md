# Projet

Ce projet est composé de deux parties : frontend et backend
## Frontend

Le frontend est développé avec [Vite](https://vitejs.dev/), un outil de développement rapide pour les applications web modernes en Vue.js.

### Installation des dépendances

```bash
cd frontend
npm install
```

### Construction de l'image Docker

```bash
cd frontend
docker build -t vite-server .
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

### Exécution de Redis en tant que conteneur Docker

```bash
docker run --name myredis --rm -p 6379:6379 redis
```

### Exécution du projet avec Docker Compose

```bash
docker-compose up
```

Après avoir démarré les conteneurs Docker, vous pouvez accéder à l'expérience à l'URL suivante :

[http://localhost:5173/signin](http://localhost:5173/signin)
