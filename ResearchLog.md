## Día 1 - Inicio real del proyecto MIRA

Fecha: 15 de mayo de 2026

Objetivo del día:
Iniciar formalmente el proyecto MIRA, ordenar su estructura inicial en GitHub y comenzar el primer bloque de aprendizaje técnico desde cero.

Qué hice hasta ahora:
- Creé el repositorio MIRA en GitHub.
- Definí el nombre del proyecto: MIRA, Monitoring Intelligence for Risk Anticipation.
- Creé la estructura inicial de carpetas del proyecto.
- Dejé preparadas las carpetas principales: data, docs, hardware, images, notebooks, reports y src.
- Creé o actualicé el archivo README.md con la presentación general del proyecto.
- Creé el archivo ResearchLog.md para registrar el avance técnico.
- Dejé el proyecto público y ordenado para comenzar a construir evidencia real.

Qué aprendí hasta ahora:
- GitHub sirve para guardar el proyecto, mostrar avances y dejar evidencia del proceso.
- Un repositorio ordenado ayuda a que otras personas entiendan qué estoy construyendo.
- El README.md sirve para presentar el proyecto.
- El ResearchLog.md sirve como bitácora técnica.
- La bitácora no es un diario personal, sino un registro de aprendizaje, decisiones, errores, avances y próximos pasos.
- MIRA debe empezar con una versión simple antes de avanzar hacia mapas, datos satelitales, inteligencia artificial y alertas.

Qué voy a hacer ahora:
- Crear mi primer archivo de práctica en Python.
- Aprender qué son variables, textos, números y la función print.
- Aprender a pedir datos con input.
- Aprender a usar condicionales simples con if, elif y else.
- Crear un primer clasificador simple de riesgo de acumulación de agua.
- Probar el código con distintos ejemplos.
- Guardar el avance en GitHub mediante un commit.

Primer objetivo técnico:
Construir una versión muy simple de MIRA v0.1 que pueda pedir datos básicos de una zona y clasificar el riesgo como bajo, medio o alto.

Ejemplo de lógica inicial:
- Si llueve mucho, aumenta el riesgo.
- Si la zona está cerca de un arroyo, río o canal, aumenta el riesgo.
- Si la zona es baja o plana, aumenta el riesgo.
- Con esos factores, MIRA calcula un puntaje simple.

Estado actual del proyecto:
- El repositorio ya existe.
- Las carpetas iniciales ya están creadas.
- Todavía estoy comenzando con programación.
- El proyecto está en etapa de base técnica.
- La prioridad actual no es hacer inteligencia artificial, sino aprender a programar y construir una primera lógica de riesgo.

Dudas actuales:
- Necesito aprender dónde se escribe código.
- Necesito aprender cómo ejecutar un archivo de Python.
- Necesito entender mejor la diferencia entre README, ResearchLog y archivos de código.
- Necesito practicar GitHub para guardar avances correctamente.

Próximo paso:
Crear el archivo `dia_1_python.py` dentro de la carpeta `src` y escribir el primer código de práctica para MIRA.

Criterio de cierre del día:
El Día 1 estará completo cuando tenga:
- ResearchLog.md actualizado.
- Un primer archivo de Python creado.
- Un clasificador simple de riesgo funcionando.
- Un commit guardado en GitHub con el avance del día.


---

## Día 2 - Prueba de MIRA v0.1 e inicio de MIRA v0.2

Fecha: 18 de mayo de 2026

Objetivo del día:
Revisar la estructura del repositorio, confirmar que MIRA v0.1 funciona correctamente y comenzar a proyectar la versión MIRA v0.2.

Qué hice:
- Abrí y trabajé con el repositorio MIRA en VSCode.
- Revisé la estructura inicial del proyecto.
- Confirmé que el proyecto cuenta con las carpetas principales:
  - data
  - docs
  - hardware
  - images
  - notebooks
  - reports
  - src
- Confirmé que el proyecto ya tiene archivos importantes:
  - README.md
  - ResearchLog.md
  - .gitignore
- Revisé el contenido del README.md, donde MIRA aparece presentado como un proyecto de investigación e ingeniería ambiental.
- Revisé el ResearchLog.md, que funciona como bitácora técnica del proyecto.
- Detecté que había una carpeta src dentro de otra carpeta src.
- Aclaré que no conviene crear una carpeta src para cada versión, sino mantener una sola carpeta src principal.
- Dejé la estructura del proyecto corregida, con una sola carpeta principal src.
- Confirmé que la estructura del proyecto quedó bien organizada.
- Confirmé que los cambios se subieron correctamente a GitHub.
- Revisé el código de mira_v0_1.py.
- Analicé la lógica del código: el programa pide datos de una zona, calcula un puntaje de riesgo y clasifica el resultado como riesgo bajo, medio o alto.
- Probé el código de MIRA v0.1 y confirmé que funcionó correctamente.
- Dejé encaminado el cierre de MIRA v0.1 como primera versión base del proyecto.
- Comencé la planificación inicial de MIRA v0.2.
- Definí que MIRA v0.2 se enfocará en empezar a trabajar con datos climáticos simples, especialmente mediante archivos CSV.
- Acordé que la v0.2 marcará el paso desde un clasificador manual hacia un sistema que pueda leer datos organizados y analizarlos.

Código probado:
El archivo probado fue:

src/mira_v0_1.py

Descripción del funcionamiento:
El programa solicita información básica sobre una zona piloto:
- nombre de la zona;
- lluvia acumulada en milímetros;
- cercanía a un arroyo, río o canal;
- si la zona es baja o plana.

A partir de esos datos, el programa calcula un puntaje simple de riesgo y clasifica el nivel como:
- bajo;
- medio;
- alto.

Resultado de la prueba:
El código de MIRA v0.1 se ejecutó correctamente.  
El programa permitió ingresar datos, calcular el puntaje de riesgo y mostrar el nivel de riesgo correspondiente.

Qué aprendí:
- Aprendí que la estructura del proyecto debe mantenerse clara y ordenada.
- Aprendí que la carpeta src debe contener el código fuente principal del proyecto.
- Aprendí que no conviene duplicar carpetas src ni crear una carpeta src diferente para cada versión.
- Aprendí que GitHub sirve para registrar y verificar el avance técnico del proyecto.
- Aprendí que MIRA v0.1 ya puede ejecutar una primera lógica simple de clasificación de riesgo.
- Aprendí que antes de avanzar a una nueva versión conviene revisar, probar y documentar correctamente la versión anterior.
- Aprendí que MIRA v0.2 debe avanzar hacia el trabajo con datos organizados, no solamente con datos ingresados manualmente.

Estado actual:
MIRA v0.1 ya cuenta con una estructura ordenada, documentación inicial, bitácora técnica y un primer archivo Python funcional.

MIRA v0.1 funciona como un clasificador simple de riesgo de acumulación de agua basado en datos ingresados manualmente.

Inicio de MIRA v0.2:
La próxima versión se enfocará en el manejo inicial de datos climáticos simples.

Objetivo inicial de MIRA v0.2:
Crear un archivo CSV con datos climáticos de prueba y desarrollar un programa capaz de leer esos datos para analizarlos de forma básica.

Próximos pasos:
- Crear un archivo CSV de prueba en la carpeta data.
- Incluir datos simples como fecha, zona, lluvia acumulada, humedad y temperatura.
- Crear el archivo src/mira_v0_2.py.
- Aprender a leer archivos CSV con Python.
- Aplicar una lógica básica de clasificación de riesgo a varios registros climáticos.
- Registrar los avances en el ResearchLog.
- Guardar los cambios en GitHub mediante commit y push.

Conclusión del día:
Hoy MIRA avanzó desde una base inicial organizada hacia un primer funcionamiento real.  
La versión v0.1 fue probada correctamente y el proyecto quedó preparado para comenzar MIRA v0.2, donde se empezará a trabajar con datos climáticos simples y organizados.