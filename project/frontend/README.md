# Social Network Frontend

Ce projet représente le frontend d'un réseau social basé sur React. Il permet aux utilisateurs de consulter leur timeline, de rechercher des profils d'utilisateurs, de consulter des sujets populaires et d'interagir avec d'autres utilisateurs en publiant des tweets.


## Choix de langage

React a été choisi pour cette application Tweet en raison de sa popularité, de sa facilité de développement et de sa performance. 

## Fonctionnalités principales

- Affichage de la timeline des tweets
- Recherche de profils utilisateur
- Affichage des sujets populaires
- Affichage des tweets associés a un sujet
- Publication de nouveaux tweets
- Navigation entre les pages de profil utilisateur et la timeline principale

## Structure du projet

Le projet est organisé comme suit :

- **`src/components`**: Contient les composants réutilisables de l'application, tels que la timeline, le formulaire de tweet, etc.
  - **`src/components/Layout.tsx`**: Le composant Layout représente la mise en page globale de l'application, y compris l'en-tête, la navigation et la section principale.
  - **`src/components/Loader.tsx`**: Le composant Loader affiche une icône de chargement pendant le chargement des données.
  - **`src/components/SearchInput.tsx`**: Le composant SearchInput est un champ de recherche réutilisable avec une icône de loupe.
  - **`src/components/Timeline.tsx`**: Le composant Timeline affiche une liste de tweets.
  - **`src/components/Topics.tsx`**: Le composant Topics affiche une liste de sujets populaires avec des liens.
  - **`src/components/Tweet.tsx`**: Le composant Tweet affiche un tweet individuel avec la possibilité de repost.

- **`src/hooks`**: Contient les hooks personnalisés utilisés dans l'application, comme `useTweets` et `useTopics`.
  - **`src/hooks/useTweets.ts`**: Le hook useTweets est utilisé pour récupérer les tweets en fonction des options spécifiées, telles que le sujet ou l'utilisateur.
  - **`src/hooks/useTopics.ts`**: Le hook useTopics est utilisé pour récupérer la liste des sujets populaires.

- **`src/pages`**: Contient les composants de page de l'application, tels que la page d'accueil et la page de profil utilisateur.
  - **`src/pages/Home.tsx`**: La page d'accueil affiche la timeline principale et les fonctionnalités de recherche d'utilisateur et de sujets.
  - **`src/pages/User.tsx`**: La page de profil utilisateur affiche les tweets d'un utilisateur spécifique.

- **`src/config.ts`**: Fichier de configuration de l'application, contenant l'URL de l'API backend.
- **`src/App.tsx`**: Point d'entrée de l'application, définissant les routes et la structure globale de l'interface utilisateur.
