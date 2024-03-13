# Flux de travail GitHub Actions pour le projet Twitter Clone

Ce flux de travail contient plusieurs tâches pour automatiser la construction et le déploiement du projet Twitter Clone.

## Flask Docker Build & Push

Ce flux de travail construit l'image Docker du backend Flask et la pousse vers Docker Hub.

### Déclencheurs

- Exécuté manuellement depuis l'onglet Actions.
- Déclenché à chaque push sur la branche principale.

### Tâches

1. **Checkout Repository**: Récupère le code source du dépôt GitHub.
2. **Set up Docker Buildx**: Configure Buildx pour construire des images multi-plateformes.
3. **Build and Push Backend Docker Image**: Construit l'image Docker du backend Flask et la pousse vers Docker Hub.

## Vite CI

Ce flux de travail vérifie, construit et teste le frontend Vite de l'application.

### Déclencheurs

- Déclenché à chaque push sur les branches principale et refactor-api.
- Déclenché à chaque pull request sur la branche principale.

### Tâches

1. **Checkout**: Récupère le code source du dépôt GitHub.
2. **Set NPM_CONFIG_CACHE**: Définit la variable d'environnement `NPM_CONFIG_CACHE`.
3. **Use Node.js**: Configure l'environnement Node.js.
4. **Install Dependencies**: Installe les dépendances npm.
5. **Build**: Compile les fichiers du projet Vite.
6. **Linter**: Vérifie la syntaxe et le style du code JavaScript.

## Deploy Vite Project to GitHub Pages

Ce flux de travail déploie automatiquement le frontend Vite sur GitHub Pages après chaque push sur la branche principale.

### Déclencheurs

- Déclenché à chaque push sur la branche principale.

### Tâches

1. **Checkout**: Récupère le code source du dépôt GitHub.
2. **Set NPM_CONFIG_CACHE**: Définit la variable d'environnement `NPM_CONFIG_CACHE`.
3. **Set up Node.js**: Configure l'environnement Node.js.
4. **Install Dependencies**: Installe les dépendances npm.
5. **Build**: Compile les fichiers du projet Vite.
6. **Configure Pages**: Configure le déploiement sur GitHub Pages.
7. **Upload artifact**: Télécharge les fichiers construits en tant qu'artefacts d'action.
8. **Deploy to GitHub Pages**: Déploie les fichiers construits sur GitHub Pages.

## Vite Docker Build & Push

Ce flux de travail construit l'image Docker du frontend Vite et la pousse vers Docker Hub.

### Déclencheurs

- Exécuté manuellement depuis l'onglet Actions.
- Déclenché à chaque push sur la branche dev.

### Tâches

1. **Checkout Repository**: Récupère le code source du dépôt GitHub.
2. **Set up Docker Buildx**: Configure Buildx pour construire des images multi-plateformes.
3. **Build and Push Frontend Docker Image**: Construit l'image Docker du frontend Vite et la pousse vers Docker Hub.
