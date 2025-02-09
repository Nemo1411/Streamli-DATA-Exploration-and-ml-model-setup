# Tableau de Bord Interactif avec Streamlit

Ce projet est une application interactive développée avec **Streamlit** permettant l'exploration et l'analyse de données, ainsi que l'entraînement de modèles de machine learning.

## Fonctionnalités
- **Page 1 (Exploration de données)** :
  - Chargement de fichiers CSV.
  - Filtrage et visualisation des données sous différentes formes (tableau, histogramme, barres, lignes, camembert).

- **Page 2 (Modélisation Machine Learning)** :
  - Chargement de données.
  - Sélection des features et de la cible.
  - Choix du modèle (Random Forest, Régression Logistique, SVM).
  - Entraînement et évaluation du modèle.
  - Sauvegarde du modèle.

- **Gestion des rôles** :
  - Authentification avec sélection de rôles (`DataManager`, `Manager`, `Admin`).
  - Accès conditionnel aux différentes pages en fonction du rôle.

## Installation
### Prérequis
- Python 3.8+
- **Pip** installé

### Installation des dépendances
```sh
pip install -r requirements.txt
```

### Lancer l'application localement
```sh
streamlit run app.py
```

## Déploiement sur Microsoft Azure
### Étape 1 : Préparer l'environnement Azure
1. **Créer une ressource Azure App Service** via le portail Azure ou la ligne de commande :
   ```sh
   az webapp create --resource-group <nom-du-groupe> --plan <nom-du-plan> --name <nom-de-l-app> --runtime "PYTHON|3.8"
   ```

2. **Activer le service Azure Storage** si vous avez des fichiers statiques ou des modèles sauvegardés.

### Étape 2 : Déployer l'application
#### Option 1 : Déploiement avec GitHub Actions (recommandé)
1. Pousser votre code sur un repo GitHub.
2. Dans Azure, activer **GitHub Actions** et suivre les instructions pour lier votre repo.
3. Une fois activé, chaque `git push` déclenchera automatiquement un déploiement.

#### Option 2 : Déploiement avec Azure CLI
1. Se connecter à Azure :
   ```sh
   az login
   ```
2. Déployer l'application :
   ```sh
   az webapp up --name <nom-de-l-app>
   ```

### Étape 3 : Configurer les variables d'environnement (si nécessaire)
Dans le portail Azure, sous **Configuration > Paramètres d'application**, ajouter les variables d'environnement requises (ex : chemins vers les fichiers modèles).

### Étape 4 : Tester l'application en ligne
Accédez à votre application via l'URL fournie par Azure :
```
https://<nom-de-l-app>.azurewebsites.net
```

## Auteur
Développé par [Votre Nom].

## Licence
Ce projet est sous licence MIT.


