# Choc thermique d’une tuyauterie épaisse avec Code_Aster

Ce projet a pour objectif d’étudier, de manière progressive, la réponse
thermomécanique transitoire d’une tuyauterie épaisse soumise à un refroidissement
de sa paroi interne et à une pression interne.

Il s’agit d’un démonstrateur générique destiné à approfondir la pratique de la
simulation thermomécanique avec **Salome-Meca et Code_Aster**, dans un contexte
inspiré des problématiques du secteur nucléaire.

> **État du projet : définition de la démarche.** La géométrie, le maillage, les
> chargements et les résultats ne sont pas encore finalisés. Ils seront ajoutés
> progressivement, uniquement après exécution et vérification.

## Environnement de travail

L’ensemble de l’étude sera réalisé dans Salome-Meca :

- module de géométrie et de maillage de Salome-Meca ;
- **AsterStudy** pour la préparation et l’exécution des calculs Code_Aster ;
- **ParaVis** pour le post-traitement et la visualisation des résultats.

Le maillage ne sera pas généré par un script Python.

## Démarche prévue

1. Définir le problème physique et les hypothèses.
2. Construire la géométrie dans l’interface de Salome-Meca.
3. Créer les groupes géométriques nécessaires.
4. Réaliser le maillage et vérifier sa qualité.
5. Effectuer un premier calcul thermique transitoire sous AsterStudy.
6. Vérifier les résultats thermiques et la convergence temporelle.
7. Effectuer séparément un calcul mécanique sous pression.
8. Comparer le cas mécanique aux équations analytiques de Lamé.
9. Réaliser le chaînage thermomécanique.
10. Post-traiter les résultats dans ParaVis.
11. Étudier la convergence du maillage et interpréter les résultats.

## Principales grandeurs à étudier

- évolution de la température dans l’épaisseur ;
- gradient thermique radial ;
- déplacement radial ;
- contraintes radiale, circonférentielle et axiale ;
- contrainte équivalente de von Mises ;
- évolution temporelle aux points intérieur, médian et extérieur.

## Contenu actuel

```text
.
├── README.md
├── docs/
│   ├── modelisation.md
│   └── verification.md
└── results/
    └── README.md
```

Les fichiers de calcul, le maillage et les images seront publiés plus tard,
après leur création et leur validation dans Salome-Meca.

## Avertissement

Les futures dimensions, propriétés et sollicitations seront génériques et
documentées. Ce projet ne constituera ni une étude de sûreté nucléaire, ni une
justification réglementaire, ni une vérification conforme au RCC-M.

## English summary

This project will progressively investigate the transient thermomechanical
response of a generic thick-walled pipe subjected to internal cooling and
pressure. Geometry creation, meshing, Code_Aster analyses and post-processing
will be performed entirely within Salome-Meca, using AsterStudy and ParaVis.

Only completed and verified modelling stages will be published. The project is
intended for learning and portfolio review, not for nuclear safety assessment
or RCC-M qualification.

## Auteur

**Oumar Mbengue** — Génie mécanique, calcul par éléments finis et simulation numérique.
