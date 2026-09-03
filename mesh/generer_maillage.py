"""Génère avec Gmsh le maillage axisymétrique générique de la tuyauterie."""

from pathlib import Path

import gmsh


RAYON_INTERIEUR = 0.150  # m
EPAISSEUR = 0.030        # m
LONGUEUR = 0.100         # m
TAILLE_RADIALE = 0.002   # m


def main() -> None:
    gmsh.initialize()
    gmsh.model.add("tuyauterie_axisymetrique")

    r_int = RAYON_INTERIEUR
    r_ext = RAYON_INTERIEUR + EPAISSEUR

    p1 = gmsh.model.geo.addPoint(r_int, 0.0, 0.0, TAILLE_RADIALE)
    p2 = gmsh.model.geo.addPoint(r_ext, 0.0, 0.0, TAILLE_RADIALE)
    p3 = gmsh.model.geo.addPoint(r_ext, LONGUEUR, 0.0, TAILLE_RADIALE)
    p4 = gmsh.model.geo.addPoint(r_int, LONGUEUR, 0.0, TAILLE_RADIALE)

    bas = gmsh.model.geo.addLine(p1, p2)
    paroi_ext = gmsh.model.geo.addLine(p2, p3)
    haut = gmsh.model.geo.addLine(p3, p4)
    paroi_int = gmsh.model.geo.addLine(p4, p1)
    contour = gmsh.model.geo.addCurveLoop([bas, paroi_ext, haut, paroi_int])
    domaine = gmsh.model.geo.addPlaneSurface([contour])
    gmsh.model.geo.synchronize()

    gmsh.model.addPhysicalGroup(2, [domaine], name="DOMAINE")
    gmsh.model.addPhysicalGroup(1, [paroi_int], name="PAROI_INT")
    gmsh.model.addPhysicalGroup(1, [paroi_ext], name="PAROI_EXT")
    gmsh.model.addPhysicalGroup(1, [bas], name="BAS")
    gmsh.model.addPhysicalGroup(1, [haut], name="HAUT")

    gmsh.option.setNumber("Mesh.Algorithm", 6)
    gmsh.model.mesh.generate(2)

    sortie = Path(__file__).with_name("tuyauterie_axisymetrique.med")
    gmsh.write(str(sortie))
    gmsh.finalize()
    print(f"Maillage écrit dans : {sortie}")


if __name__ == "__main__":
    main()

