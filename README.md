# Choc thermique d’une tuyauterie épaisse avec Code_Aster

Ce projet étudie la réponse thermomécanique transitoire d’une tuyauterie
épaisse soumise simultanément à un refroidissement rapide de sa paroi interne
et à une pression interne. Il constitue un démonstrateur générique inspiré des
problématiques rencontrées sur les circuits industriels sous pression,
notamment dans le secteur nucléaire.

> **Statut : préparation du modèle.** Aucun résultat de calcul n’est encore
> présenté. Les dimensions, propriétés et chargements sont fictifs et ne
> décrivent aucune installation réelle.

## Objectifs

- calculer la diffusion transitoire de la température dans l’épaisseur ;
- transférer le champ thermique vers un calcul mécanique axisymétrique ;
- combiner la dilatation thermique et la pression interne ;
- suivre les contraintes radiale, circonférentielle, axiale et de von Mises ;
- déterminer l’instant et la zone les plus sollicités ;
- vérifier la convergence spatiale et temporelle ;
- comparer les résultats à des solutions analytiques simples.

## Démarche numérique

1. Création d’un maillage axisymétrique de la paroi de la tuyauterie.
2. Calcul thermique transitoire sous Code_Aster.
3. Transfert du champ de température vers le modèle mécanique.
4. Application de la pression interne et des conditions aux limites.
5. Calcul des déplacements, déformations et contraintes à chaque instant.
6. Vérifications analytiques et études de convergence.

## Modèle initial proposé

| Paramètre | Valeur initiale de démonstration |
|---|---:|
| Rayon intérieur | 150 mm |
| Épaisseur | 30 mm |
| Longueur modélisée | 100 mm |
| Température initiale | 300 °C |
| Température finale du fluide | 50 °C |
| Durée de refroidissement imposée | 30 s |
| Pression interne | 15,5 MPa |
| Formulation | Axisymétrique |

Ces valeurs devront être soumises à une étude de sensibilité. Elles ne sont pas
issues d’un cahier des charges industriel.

## Organisation du dépôt

```text
.
├── README.md
├── docs/
│   ├── modelisation.md
│   └── verification.md
├── mesh/
│   └── generer_maillage.py
├── case/
│   └── calcul_thermomecanique.comm
└── results/
    └── README.md
```

## Outils prévus

- **Salome-Meca / Gmsh** : géométrie, groupes physiques et maillage ;
- **Code_Aster** : calcul thermique transitoire et calcul mécanique ;
- **ParaVis / ParaView** : visualisation des champs ;
- **Python** : courbes, comparaisons et études paramétriques.

## Grandeurs à analyser

- température dans l’épaisseur en fonction du temps ;
- gradient thermique radial ;
- déplacement radial ;
- contraintes radiale, circonférentielle et axiale ;
- contrainte équivalente de von Mises ;
- évolution temporelle aux points intérieur, médian et extérieur.

## Avertissement

Ce dépôt est destiné à l’apprentissage et à la présentation d’une démarche de
simulation. Il ne constitue ni une étude de sûreté, ni une justification
réglementaire, ni une vérification conforme au RCC-M.

## English summary

This project investigates the transient thermomechanical response of a generic
thick-walled pipe subjected to internal cooling and pressure. The planned
workflow includes an axisymmetric transient thermal analysis, temperature-field
transfer to mechanics, stress post-processing and analytical verification.

The model uses fictional public data and is intended for learning and portfolio
review only. It is not a nuclear safety assessment or an RCC-M qualification.

## Auteur

**Oumar Mbengue** — Génie mécanique, calcul par éléments finis et simulation numérique.

