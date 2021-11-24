# Analyse comparative Consommation CO2 - Basé sur le One Byte Model

## Définition
L'application a deux objectifs :
- Mesurer l'impact Carbone de la lecture d'une page web
Sont pris en compte : 
  - La consommation du data center
  - La consommation du réseau
  - Le coût d'utilisation de l'appareil
- Comparer l'impact Carbone sur un an d'utilisation de plusieurs produits en fonction de leur lieu d'utilisation 
Sont pris en compte : 
  - La fabrication des produits
  - La consommation du data center
  - La consommation du réseau
  - Le coût d'utilisation de l'appareil

 
## Description - lecture d'une page web

### Rentrer le poids de la page et le temps de lecture
> Le poids est trouvable avec la console JavaScript de Chrome ou Firefox.

### Choix du type d'appareil, du réseau, et du lieu de travail
> L'impact énergétique dépend beaucoup de lieu de travail et de l'origine de l'énergie de chaque pays.

S'affichent alors les calculs des Bilan Carbone et de la consommation énergétique totale de la lecture d'une page web.
> Les deux graphes représentent la proportion du score détenu par chacune des sous-parties.
 
## Description - Comparatif

### Rentrer la quantité de données moyenne utilisée par jour de travail et l’âge actuel de l'appareil 
> Une base de calcul est proposée par Orange. Le lien est le suivant : https://www.orange.ma/Offres-services/Simulateur

> L’âge permet de calculer le cout annuel de l'appareil. Plus un appareil est récent, plus son cout annuel est important. 

### Choix des couleurs des légendes
Les couleurs sont modifiables pour les camemberts suivants

S'affiche alors 30 graphiques. 24 camemberts correspondant à la comparaison de 4 combinaisons d'appareils dans 6 pays/régions du monde. 
> le drapeau bleu avec les 6 cercles correspond au drapeau de la terre (il s'agit ici d'une moyenne mondiale). 

Les barplots représentent la consommation totale de chacun des appareils pour le pays ou la région correspondante (1 étant Laptop et 4 Smartphone)

## Contenu du Git

### Le Git doit absolument contenir les éléments suivants :
- le dossier ONE_BYTE contenant :
  - le fichier CO2_Comparison.py (l'application).
- un fichier requirements.txt contenant :
  ```ruby
  matplotlib==3.5.0
  seaborn==0.11.0
  ```
- un dossier app_logos contenant les images des drapeaux des différents pays  
  
### Il peut également contenir :
 - Les images des logos à afficher dans le dossier app_logos 
 - Un dossier .streamlit contenant un fichier .config.toml avec le contenu suivant :  
    ```ruby

    [theme]

    # The preset Streamlit theme that your custom theme inherits from. One of "light" or "dark".
    base = "light"

    # Primary accent color for interactive elements.
    primaryColor = "#******"

    # Background color for the main content area.
    #backgroundColor =

    # Background color used for the sidebar and most interactive widgets.
    secondaryBackgroundColor = "#******"

    # Color used for almost all text.
    textColor = "#******"

    # Font family for all text in the app, except code blocks. One of "sans serif", "serif", or "monospace".
    #font =
    ```
    > "#******" --> A compléter avec les couleurs choisies 

## Déploiement sur Streamlit

### 1. Création d'un compte
Tout d'abord il faut créer un compte sur <https://share.streamlit.io/>
  > la version "*Community*" autorise 3 applications mais qui doivent se trouver sur un *repository* Git publique.
  >
  > La version "*Teams*" coute 250$ mensuel et permet le déploiement de 10 applications privées. 


### 2. Ajout d'une nouvelle App
- Cliquer sur *New app*
- Sélectionner le *repository* git 
- Sélectionner la branche
- Sélectionner l'application à déployer 
- Cliquer sur *deploy*

### 3. Une fois l'application déployée
- Revenir sur <https://share.streamlit.io/> et se connecter
- Cliquer sur les ... verticaux à droite du nom de l'app 
- Cliquer sur *settings*
- Cliquer sur *secrets*
