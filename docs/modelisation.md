# Hypothèses de modélisation

## Géométrie

La tuyauterie droite est représentée par sa section méridienne dans le plan
$(r,z)$. L’hypothèse axisymétrique permet de réduire le modèle 3D à un domaine
rectangulaire correspondant à la paroi.

## Hypothèses thermiques

- matériau homogène et isotrope ;
- température initiale uniforme ;
- convection imposée sur la paroi interne ;
- paroi externe adiabatique dans la première version ;
- absence de rayonnement et de source thermique volumique ;
- propriétés constantes dans la première version, puis dépendantes de la
  température dans une évolution ultérieure.

## Hypothèses mécaniques

- comportement élastique linéaire isotrope ;
- petites déformations et petits déplacements ;
- chargement axisymétrique ;
- pression uniforme sur la paroi interne ;
- blocage axial minimal destiné à supprimer les mouvements de corps rigide ;
- absence initiale de plasticité, de fluage, de soudure et de défaut.

## Chaînage thermomécanique

Le calcul est séquentiel : le champ de température est d’abord obtenu sur tous
les instants du transitoire, puis utilisé comme variable de commande du calcul
mécanique. L’effet de la mécanique sur le problème thermique est négligé.

## Groupes de maillage

| Groupe | Fonction |
|---|---|
| `DOMAINE` | Paroi de la tuyauterie |
| `PAROI_INT` | Convection et pression internes |
| `PAROI_EXT` | Condition thermique externe |
| `BAS` | Blocage axial minimal |
| `HAUT` | Extrémité opposée |

## Étapes d’évolution

1. Propriétés thermiques et mécaniques constantes.
2. Propriétés dépendantes de la température.
3. Raffinement local et convergence temporelle.
4. Comportement élastoplastique avec `STAT_NON_LINE` si nécessaire.
5. Cycles répétés et étude exploratoire de fatigue thermique.

