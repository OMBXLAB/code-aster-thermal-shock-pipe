# Préparation de la modélisation

Ce document rassemble les choix qui devront être définis et justifiés avant la
création du modèle dans Salome-Meca. Les hypothèses ci-dessous ne sont pas
encore figées.

## Géométrie à définir

- dimensions génériques de la tuyauterie ;
- longueur représentative du tronçon étudié ;
- modèle axisymétrique ou tridimensionnel ;
- influence éventuelle des effets d’extrémité.

Une formulation axisymétrique pourra être retenue si la géométrie, les
conditions aux limites et les chargements sont invariants autour de l’axe.

## Modèle thermique à définir

- température initiale ;
- évolution temporelle de la température du fluide interne ;
- coefficient d’échange convectif interne ;
- condition thermique appliquée à la paroi externe ;
- conductivité, masse volumique et capacité thermique du matériau ;
- dépendance éventuelle des propriétés à la température ;
- durée du transitoire et discrétisation temporelle.

## Modèle mécanique à définir

- pression interne ;
- module de Young, coefficient de Poisson et coefficient de dilatation ;
- conditions aux limites nécessaires sans surcontraindre la structure ;
- représentation ou non des effets de fond ;
- comportement thermoélastique ou élastoplastique ;
- dépendance éventuelle des propriétés à la température.

## Groupes à préparer dans Salome-Meca

Les noms définitifs seront choisis lors de la construction de la géométrie et
du maillage. Il faudra au minimum identifier :

- le domaine matériel ;
- la paroi intérieure ;
- la paroi extérieure ;
- les extrémités du tronçon ;
- les lignes ou surfaces nécessaires à l’extraction des résultats.

## Chaînage envisagé

Le calcul thermomécanique sera séquentiel : le champ de température transitoire
sera d’abord calculé, vérifié et sauvegardé. Il sera ensuite utilisé comme
variable de commande dans le calcul mécanique.

Les commandes Code_Aster ne seront ajoutées au dépôt qu’après leur création et
leur exécution dans AsterStudy.
