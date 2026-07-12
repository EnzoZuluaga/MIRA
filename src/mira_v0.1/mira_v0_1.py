"""
MIRA v0.1
Monitoring Intelligence for Risk Anticipation

Primera versión ejecutable del proyecto.
Objetivo: clasificar de forma simple el riesgo de acumulación de agua
en una zona piloto usando tres factores básicos.

Este archivo NO es la versión final del sistema.
Es una primera versión funcional para aprender, probar y documentar.
"""

# -------------------------------
# MIRA v0.1 - Clasificador simple
# -------------------------------

def clasificar_riesgo(lluvia_mm, cerca_agua, zona_baja):
    """
    Calcula un puntaje simple de riesgo.

    Factores:
    - lluvia acumulada alta
    - cercanía a arroyo, río o canal
    - zona baja o plana
    """

    riesgo = 0

    if lluvia_mm >= 50:
        riesgo += 1

    if cerca_agua == "si":
        riesgo += 1

    if zona_baja == "si":
        riesgo += 1

    if riesgo == 0:
        nivel = "bajo"
    elif riesgo == 1:
        nivel = "medio"
    else:
        nivel = "alto"

    return riesgo, nivel


def main():
    print("MIRA v0.1 - Clasificador simple de riesgo de acumulación de agua")
    print("---------------------------------------------------------------")

    zona = input("Ingrese el nombre de la zona piloto: ")
    lluvia_mm = int(input("Ingrese lluvia acumulada en mm: "))
    cerca_agua = input("¿Está cerca de un arroyo, río o canal? si/no: ").lower()
    zona_baja = input("¿La zona es baja o plana? si/no: ").lower()

    puntaje, nivel = clasificar_riesgo(lluvia_mm, cerca_agua, zona_baja)

    print("")
    print("Resultado del análisis")
    print("----------------------")
    print("Zona analizada:", zona)
    print("Lluvia acumulada:", lluvia_mm, "mm")
    print("Puntaje de riesgo:", puntaje)
    print("Nivel de riesgo:", nivel.upper())


if __name__ == "__main__":
    main()
