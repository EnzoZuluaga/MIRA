print("--------------------------------------------------------------------------")
print("EVALUACIÓN DE RIESGO DE DESASTRES NATURALES EN UNA ZONA ESPECÍFICA")
print("--------------------------------------------------------------------------")
print("Ingrese los siguientes datos para evaluar el riesgo de desastres naturales en la zona:")
print("--------------------------------------------------------------------------")
zona = input("Ingrese la zona que desea analizar: ")
lluvia_acumulada = float(input("Ingrese la cantidad de lluvia acumulada en mm: "))
humedad_ambiente = float(input("Ingrese la humedad ambiente en porcentaje: "))
temperatura = float(input("Ingrese la temperatura en grados Celsius: "))
velocidad_viento = float(input("Ingrese la velocidad del viento en km/h: "))
puntaje_riesgo_lluvia = 0
puntaje_riesgo_humedad = 0
puntaje_riesgo_temperatura = 0
puntaje_riesgo_viento = 0



if lluvia_acumulada > 50:
    puntaje_riesgo_lluvia += 3
    print("Destaco alerta: lluvia intensa, posible inundación.")
elif lluvia_acumulada > 20:
    puntaje_riesgo_lluvia += 2
elif lluvia_acumulada > 10:
    puntaje_riesgo_lluvia += 1

if humedad_ambiente > 80:
    puntaje_riesgo_humedad += 3
    print("Destaco alerta: alta humedad, riesgo de enfermedades respiratorias.")
elif humedad_ambiente > 60:
    puntaje_riesgo_humedad += 2
elif humedad_ambiente > 40:
    puntaje_riesgo_humedad += 1

if temperatura > 50:
    puntaje_riesgo_temperatura += 3
    print("Destaco alerta: temperatura alta, riesgo de deshidratación.")
elif temperatura > 40:
    puntaje_riesgo_temperatura += 2
elif temperatura > 30:
    puntaje_riesgo_temperatura += 1


if temperatura < -10:
    puntaje_riesgo_temperatura += 3
    print("Destaco alerta: temperatura baja, riesgo de hipotermia.")
elif temperatura < 0:
    puntaje_riesgo_temperatura += 2
elif temperatura < 10:
    puntaje_riesgo_temperatura += 1

if velocidad_viento > 50:
    puntaje_riesgo_viento += 3
    print("Destaco alerta: viento fuerte, riesgo de daños estructurales.")
elif velocidad_viento > 30:
    puntaje_riesgo_viento += 2
elif velocidad_viento > 10:
    puntaje_riesgo_viento += 1

puntaje_riesgo = puntaje_riesgo_lluvia + puntaje_riesgo_humedad + puntaje_riesgo_temperatura + puntaje_riesgo_viento

print(f"El puntaje de riesgo para la zona {zona} es: {puntaje_riesgo}")

nivel_riesgo = ""
recomendacion = ""

if puntaje_riesgo >= 11:
    nivel_riesgo = "Extremo"
    recomendacion = "prohibido salir y postergar actividades al aire libre."

elif puntaje_riesgo >= 9:
    nivel_riesgo = "Alto"
    recomendacion = "Se recomienda evitar salir y postergar actividades al aire libre."

elif puntaje_riesgo >= 5:
    nivel_riesgo = "Moderado"
    recomendacion = "Se recomienda salir con precaución y evitar actividades al aire libre."

else:
    nivel_riesgo = "Bajo"
    recomendacion = "Se recomienda salir con normalidad y realizar actividades al aire libre."
print("--------------------------------------------------------------------------")
print("DETALLE DEL PUNTAJE DE RIESGO:")
print(f"Lluvia: {puntaje_riesgo_lluvia} puntos")
print(f"Humedad: {puntaje_riesgo_humedad} puntos")
print(f"Temperatura: {puntaje_riesgo_temperatura} puntos")
print(f"Viento: {puntaje_riesgo_viento} puntos")
print("--------------------------------------------------------------------------")
print(f"El nivel de riesgo para la zona {zona} es: {nivel_riesgo}")
print("--------------------------------------------------------------------------")
print(f"Recomendación: {recomendacion}")
