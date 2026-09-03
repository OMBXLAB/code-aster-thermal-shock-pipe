# Plan de vérification

## Vérification thermique

- contrôler l’uniformité du champ à l’instant initial ;
- vérifier la direction du flux thermique ;
- comparer le régime permanent à la solution analytique de conduction radiale
  dans un cylindre épais ;
- comparer plusieurs tailles d’éléments dans l’épaisseur ;
- comparer plusieurs pas de temps pendant le refroidissement rapide ;
- contrôler qualitativement les nombres de Biot et de Fourier.

## Vérification mécanique

- vérifier la suppression des mouvements de corps rigide ;
- calculer séparément les cas « pression seule » et « thermique seul » ;
- comparer le cas « pression seule » aux équations de Lamé ;
- vérifier l’équilibre entre la pression appliquée et les réactions ;
- contrôler la continuité des déplacements et la régularité des contraintes ;
- écarter les pics associés à une singularité numérique avant interprétation.

## Étude de convergence

Les grandeurs suivantes seront suivies :

- température sur les faces intérieure et extérieure ;
- contrainte circonférentielle sur les faces intérieure et extérieure ;
- contrainte de von Mises maximale hors singularités ;
- déplacement radial maximal.

Une grandeur sera considérée stabilisée lorsque sa variation entre deux
raffinements successifs sera suffisamment faible au regard de l’objectif de
l’étude. Le seuil retenu devra être annoncé avec les résultats.

## Limites de validation

La concordance avec une solution analytique simple vérifie uniquement une
partie du modèle. Elle ne valide pas automatiquement les hypothèses physiques,
les propriétés du matériau ou la pertinence d’un calcul réglementaire.

