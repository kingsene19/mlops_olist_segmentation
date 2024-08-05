# Projet MLOPS : Segmentation des clients du site E-commerceOlist

Contributeurs :
- El Hadj Dame Lo Kaba
- Mohamed Massamba Sene
- Mamadou Wade

Ce notebook traite de la segmentation des clients d'Olist, une plateforme de commerce électronique brésilienne. Les données proviennent d'un jeu de données publiques accessibles via [Kaggle](https://www.kaggle.com/olistbr/brazilian-ecommerce).

Le commerce électronique est un modèle d'affaires qui permet aux entreprises ou aux particuliers d'acheter ou de vendre des biens via Internet. Les clients du commerce électronique ont des personnalités extrêmement variées, et un marché potentiel n'est généralement pas caractérisé de manière unique ou simple. Il devient donc crucial de connaître sa base de clients cible afin de s'assurer que vos communications soient à la fois efficaces (attractives, incitatives) et appropriées (non offensantes, opportunes et pertinentes). Comprendre les comportements des clients permet aux entreprises de regrouper différents clients en groupes.

## Présentation du sujet

Olist, une entreprise brésilienne spécialisée dans la vente sur les marketplaces en ligne, souhaite optimiser ses campagnes de communication en segmentant ses clients. Cette segmentation permettra de mieux comprendre les différents profils d'utilisateurs et de cibler les campagnes de manière plus efficace. Les clients visitent les sites de commerce électronique pour atteindre un objectif. Cet objectif peut être simple ou complexe. En analysant le comportement des utilisateurs, nous pouvons déduire des stratégies communes que les utilisateurs suivent pour atteindre un objectif. En se basant sur le comportement des clients il faut fournir une segmentation actionable et compréhensible pour l'équipe marketing d'Olist.
Les questions qui se posent deviennent donc
Comment segmenter efficacement les clients d'Olist pour permettre une communication marketing ciblée et personnalisée ? 
Quels sont les segments de clients les plus pertinents pour Olist, et comment peuvent-ils être identifiés à partir des données disponibles ?
Pour ce faire nous procédons donc comme suit:


### Etape 1: Analyse exploratoire des données
Dans cette étape nous procédons à une l'analyse du jeu de données en passant par le chargement et le nettoyage des différents dataframes avant de les fusionner. Nous poursuivons ensuite avec quelques visualisations pour avoir une meilleure compréhension du jeu de données avant de passer au feauture engineering.</br>
A la fin de cette étape nous obtenons donc notre jeu de données final qui pourra être utilisé pour les modèles

### Etape 2: Expérimentation et choix d'un modèle final
Suite à l'analyse des données, nous utilisons le notebook résultant afin de tester divers modèles de segmentation en prenant soin de déterminer les paramètres optimaux. Nous faison également le suivi avec des expériences MLFlow et déterminons le modèle final à utiliser sur la base d'une comparaison des performances.

### Etape 3: Détermination du délai de maintenance
A la suite des étapes précédentes, nous faisons des simulations afin de déterminer une fréquence appropriée de mise à jour du modèle final

### Etape 4: Mise en place de la pipeline CI/CD
Nous mettons ensuite en place une pipeline CI/CD avec Github Actions en prenant soin d'automatiser les tests unitaires, l'exécution des notebooks et le déploiement de l'API créée pour servir le modèle.

### Résulats
Une fois la pipeline exécuté à mesure que nous apportons des modifications, nous avons donc dockerisé et déployé notre API sur Render.

![Docker Image](https://i.ibb.co/vL2FjC1/olist-dockerhub.png)
![Render](https://i.ibb.co/xsZh8n1/render-deploy.png)


L'API est disponible au niveau de l'url `https://olist-segmentation-api.onrender.com` avec une documentation à l'endpoint `/docs`

![API](https://i.ibb.co/VxDmX74/api-docs.png)


Nous avons également déployé une inteface graphique streamlit pour faciliter son utilisation à l'endpoint `https://mlopsolistsegmentation-vlbfmufaw2ros9lpkdx7nq.streamlit.app/`. 
![UI](https://i.ibb.co/t3k1k1f/ui-1.png)
![UI](https://i.ibb.co/1v3BcVG/ui-2.png)

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

