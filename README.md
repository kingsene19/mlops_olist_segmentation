# Projet MLOPS : Segmentation des clients Olist

Contributeurs :
- El Hadj Dame Lo Kaba
- Mohamed Massamba Sene
- Mamadou Wade

Ce notebook traite de la segmentation des clients d'Olist, une plateforme de commerce électronique brésilienne. Les données proviennent d'un jeu de données publiques accessibles via [Kaggle](https://www.kaggle.com/olistbr/brazilian-ecommerce).

Le commerce électronique est un modèle d'affaires qui permet aux entreprises ou aux particuliers d'acheter ou de vendre des biens via Internet. Les clients du commerce électronique ont des personnalités extrêmement variées, et un marché potentiel n'est généralement pas caractérisé de manière unique ou simple. Il devient donc crucial de connaître sa base de clients cible afin de s'assurer que vos communications soient à la fois efficaces (attractives, incitatives) et appropriées (non offensantes, opportunes et pertinentes). Comprendre les comportements des clients permet aux entreprises de regrouper différents clients en groupes.

## Identification du problème

### 1. Définition du problème
Les clients visitent les sites de commerce électronique pour atteindre un objectif. Cet objectif peut être simple ou complexe. En analysant le comportement des utilisateurs, nous pouvons déduire des stratégies communes que les utilisateurs suivent pour atteindre un objectif. Au niveau le plus granulaire, le comportement des utilisateurs se manifeste par des requêtes de recherche et des interactions.

Le problème est que nous n'avons pas encore calculé la valeur RFM, pour clarifier l'analyse des données, nous devons approfondir l'analyse de la valeur RFM et diviser les clients en segments.

### 2. Objectifs
À partir des jeux de données disponiblex, nous avons constaté que nous pouvons utiliser la segmentation de clients pour le développement de l'e-commerce d'Olist afin de découvrir les habitudes de chaque segment de clients. La segmentation des clients qui sera générée par ce projet pourra ensuite aider Olist à mettre en œuvre des stratégies de publicité / marketing pour chaque segment.

L'objectif est de créer un algorithme pour le regroupement des clients afin d'aider Olist à connaître les caractéristiques des utilisateurs d'Olist. Le but principal de ce projet est d'aider à atteindre les attentes de l'algorithme à créer pour le regroupement de chaque segment d'utilisateurs à travers les objectifs suivants :

◉ Regrouper les clients en fonction de leur comportement afin qu'ils soient divisés en plusieurs segments:

◉ Découvrir les caractéristiques déterminantes dans chaque segment de clients.

Avec ces deux objectifs, cela peut aider l'équipe commerciale d'Olist à trouver des stratégies de marketing / publicité basées sur le type ou les caractéristiques de chaque cluster que nous avons formé.

### 3. Exploration et Modélisation des Données
Nous effectuons une analyse sur les jeux de données en utilisant les méthodes KMeans, DBSCAN et GaussianMixture après avoir les caractéristiques reflétant le comportement pour chaque client, puis nous appliquons la segmentation des clients. Pour la comparaison, nous utilisons également les mesures de performance suivantes pour évaluer le modèle de machine learning : le score silhouette, le score de Calinski-Harabasz et le score de Davies-Bouldin. Après cela, nous déterminons la fréquence à laquelle le modèle doit être mis à jour en fonction de l'analyse temporelle de la stabilité des clusters.

### 4. Déploiement
Ce projet étant orienté vers les pratiques MLOps, nous intégrons ces principes dans notre projet, tels que le suivi avec MLFlow ainsi qu'un pipeline CI/CD pour automatiser les tests, les exécutions de notebooks et le déploiement du modèle. Nous veillons également à respecter les conventions PEP.

## Structure du Repo

### Structure des répertoires

- [.github](#github)
- [API](#api)
- [images](#images)
- [logs](#logs)
- [notebooks](#notebooks)
- [olist_dataset](#olist_dataset)
- [output_files](#output_files)
- [reports](#reports)
- [settings](#settings)
- [src](#src)
- [UI](#ui)
- [tests](#tests)

### Descriptions des répertoires

#### .github
Contient des fichiers spécifiques à GitHub, y compris les workflows pour les pipelines CI/CD.
- `workflows/`: Contient les fichiers de workflow GitHub Actions (par exemple, `main.yml`)

#### API
Contient le code et les ressources liés à l'API.
- `data/`: Contient le jeu de données des segments de clients
- `models/`: Contient le modèle utilisé pour les prédictions
- `utils/`: Fonctions utilitaires pour l'API
- `app.py`: Fichier principal de l'application API
- `Dockerfile`: Instructions de containerisation pour l'API
- `requirements.txt`: Dépendances Python pour l'API

#### images
Stocke les ressources d'images utilisées dans les notebooks.

#### logs
Contient les sorties des exécutions des notebooks, organisées par année, mois et type de notebook (analyse, entraînement, stabilité).

#### notebooks
Notebooks Jupyter pour l'exploration des données, l'analyse et l'expérimentation.
- `mlruns/`: Fichiers de suivi MLflow
- `segmentation_01_analyse.ipynb`: Analyse des données concernant les jeux de données
- `segmentation_02_essais.ipynb`: Test et suivi du modèle
- `segmentation_03_stabilite.ipynb`: Analyse de la stabilité pour déterminer la fréquence de mise à jour

#### olist_dataset
Contient les fichiers du jeu de données de commerce électronique d'Olist.
- `olist_customers_dataset.csv`
- `olist_order_items_dataset.csv`
- `olist_order_payments_dataset.csv`
- `olist_order_reviews_dataset.csv`
- `olist_orders_dataset.csv`
- `olist_products_dataset.csv`
- `olist_sellers_dataset.csv`
- `product_category_name_translation.csv`

#### output_files
Stocke les fichiers de sortie générés lors des exécutions des notebooks.
- `olist-kmeans-current.pkl`: Modèle K-means sérialisé
- `segmentation_01_analyse_rfm_...`: Résultats finaux de l'analyse des données (jeu de données utilisé pour l'entraînement du modèle)
- `segmentation_01_analyse_step1.csv`: Résultats intermédiaires de l'analyse des données

#### reports
Contient les rapports générés.
- `olist_segmentation_profiling.html`: Profilage des données pour le jeu de données

#### settings
Contient les fichiers de configuration pour le projet.
- `params.py`: Définitions de paramètres pour le projet

#### src
Fonctions utilitaires pour les fonctionnalités principales du projet.
- `load_dataset.py`: Fonctions pour charger les jeux de données

#### tests
Contient les fichiers de test pour le projet.
- `test_datasets.py`: Tests pour le chargement et le traitement des jeux de données

#### UI
Une interface graphique streeamlit pour l'utilisation du modèle

### Fichiers clés dans le répertoire racine

- `requirements-nr.txt`: Dépendances Python non-root
- `requirements-tests.txt`: Dépendances Python pour l'exécution des tests
- `run_olist.sh`: Script shell pour exécuter les notebooks

## Interface graphique

Une fois le modèle entrainé nous mettons en place une API pour son exploitation que nous avons dockerisé et déployé sur Render à l'aide de la pipeline github actions.

![Docker Image](https://i.ibb.co/vL2FjC1/olist-dockerhub.png)
![Render](https://i.ibb.co/xsZh8n1/render-deploy.png)


L'API est disponible au niveau de l'url `https://olist-segmentation-api.onrender.com` avec une documentation à l'endpoint `/docs`

![API](https://i.ibb.co/VxDmX74/api-docs.png)


Nous avons également déployé une inteface graphique streamlit pour faciliter son utilisation à l'endpoint `https://mlopsolistsegmentation-vlbfmufaw2ros9lpkdx7nq.streamlit.app/`. 
![UI](https://i.ibb.co/t3k1k1f/ui-1.png)
![UI](https://i.ibb.co/1v3BcVG/ui-2.png)