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


## Día 3 - Profundización de condicionales y fortalecimiento de MIRA v0.1

**Fecha:** 5 de junio de 2026

### Objetivo del día

Profundizar el estudio de estructuras condicionales, tipos de datos y lógica de clasificación en Python para fortalecer la versión inicial de MIRA antes de avanzar hacia MIRA v0.2.

Aunque el próximo paso previsto era comenzar a trabajar con archivos CSV para MIRA v0.2, se decidió dedicar esta jornada a mejorar la comprensión del código base y hacer que MIRA v0.1 sea más sólida, clara y confiable.

---

### Qué hice

Trabajé sobre la lógica inicial de MIRA v0.1, enfocándome en comprender mejor cómo el programa toma datos, los procesa y genera una clasificación de riesgo.

Repasé y practiqué el uso de `input()` para solicitar información al usuario.

Reforcé el uso de `float()` para convertir datos ingresados como texto en valores numéricos que puedan ser utilizados en cálculos.

Estudié con mayor profundidad el funcionamiento de los condicionales `if`, `elif` y `else`.

Analicé la importancia del orden de las condiciones, especialmente en casos donde se evalúan valores progresivos, como lluvia acumulada, humedad, temperatura y velocidad del viento.

Comprendí que, cuando se usan condiciones como `> 50`, `> 40` y `> 30`, es necesario ordenar primero los valores más extremos para que Python evalúe correctamente el caso más grave.

También trabajé sobre el uso de puntajes separados por variable climática, creando una lógica más ordenada para lluvia, humedad, temperatura y viento.

Se agregó una estructura de puntajes parciales:

```python
puntaje_riesgo_lluvia = 0
puntaje_riesgo_humedad = 0
puntaje_riesgo_temperatura = 0
puntaje_riesgo_viento = 0
```

Luego, cada variable climática suma su propio puntaje según las condiciones ingresadas.

Después se calcula el puntaje total:

```python
puntaje_riesgo = puntaje_riesgo_lluvia + puntaje_riesgo_humedad + puntaje_riesgo_temperatura + puntaje_riesgo_viento
```

También se incorporaron alertas específicas para que el sistema no solo indique el nivel de riesgo general, sino que explique qué factor climático activó una alerta.

Ejemplos de alertas trabajadas:

* lluvia intensa y posible inundación;
* alta humedad;
* temperatura extremadamente alta;
* temperatura extremadamente baja;
* viento fuerte.

Se agregó además un detalle del puntaje por categoría, para que el resultado sea más transparente y fácil de interpretar.

---

### Código trabajado

El trabajo se realizó sobre la lógica base de MIRA v0.1, fortaleciendo el archivo principal del prototipo inicial.

El programa actualmente solicita:

* zona a analizar;
* lluvia acumulada en milímetros;
* humedad ambiente en porcentaje;
* temperatura en grados Celsius;
* velocidad del viento en km/h.

A partir de esos datos, calcula puntajes parciales y un puntaje total de riesgo.

Luego clasifica el nivel de riesgo como:

* Bajo;
* Moderado;
* Alto;
* Extremo.

Finalmente, muestra una recomendación automática según el nivel de riesgo calculado.

---

### Pruebas realizadas

Se probaron distintas tandas de datos para verificar que la lógica funcionara correctamente.

Las pruebas incluyeron casos de:

* riesgo bajo;
* riesgo moderado;
* riesgo alto;
* riesgo extremo;
* lluvia intensa;
* humedad elevada;
* frío extremo;
* calor extremo;
* viento fuerte;
* casos límite con valores cercanos a los umbrales.

El programa pasó correctamente las pruebas realizadas.

---

### Qué aprendí

Aprendí que no alcanza con escribir condiciones, sino que también es importante pensar en el orden en que Python las evalúa.

Aprendí que `input()` siempre devuelve texto, por lo que es necesario usar `float()` cuando se quiere trabajar con números.

Aprendí que una lógica basada en puntajes permite representar mejor el riesgo que una lógica basada solamente en condiciones rígidas.

Aprendí que separar el puntaje por variable hace que el programa sea más claro, más fácil de corregir y más parecido a un sistema real de análisis.

Aprendí que MIRA no debe limitarse a decir “riesgo alto” o “riesgo bajo”, sino que también debe explicar por qué llega a ese resultado.

Aprendí que antes de avanzar hacia una nueva versión grande conviene fortalecer bien la versión anterior.

Aprendí que una actualización del código inicial no necesariamente significa una nueva versión principal. En este caso, el trabajo realizado corresponde a una mejora de MIRA v0.1, no todavía a MIRA v0.2.

---

### Estado actual

MIRA v0.1 quedó más sólida que antes.

El programa ahora cuenta con una lógica más clara de clasificación de riesgo, puntajes separados por variable climática, alertas específicas y detalle del puntaje final.

Esta mejora puede considerarse una actualización interna de la versión inicial, por ejemplo:

**MIRA v0.1.1 - Mejora de lógica condicional, tipos de datos y alertas específicas**

Todavía no se comenzó formalmente MIRA v0.2, ya que se priorizó fortalecer la comprensión técnica y mejorar la calidad del código base.

---

### Decisión técnica del día

Se decidió no avanzar todavía con archivos CSV ni con lectura de datos externos.

La razón fue que antes de iniciar MIRA v0.2 era necesario comprender mejor los fundamentos de programación que sostienen el sistema:

* tipos de datos;
* entrada de datos;
* conversión numérica;
* condicionales;
* comparación de valores;
* suma de puntajes;
* clasificación de riesgo;
* recomendaciones automáticas.

Esta decisión fortalece el proyecto porque evita avanzar demasiado rápido sin comprender bien la base.

---

### Próximos pasos

Revisar nuevamente el código mejorado de MIRA v0.1.1.

Guardar los cambios en GitHub mediante commit y push.

Registrar esta actualización en el repositorio.

Luego sí, comenzar MIRA v0.2 con el objetivo previsto:

* crear un archivo CSV de prueba en la carpeta `data`;
* incluir datos simples como fecha, zona, lluvia acumulada, humedad, temperatura y viento;
* crear el archivo `src/mira_v0_2.py`;
* aprender a leer archivos CSV con Python;
* aplicar la lógica de clasificación de riesgo a varios registros climáticos;
* comparar resultados entre distintas zonas o fechas.

---

### Conclusión del día

Hoy MIRA no avanzó hacia una nueva versión grande, sino que fortaleció su base técnica.

El trabajo del día fue importante porque permitió comprender mejor cómo funcionan los condicionales, los tipos de datos y la lógica de puntajes en Python.

MIRA v0.1 ahora es más clara, más explicativa y más sólida. Esta base será necesaria para que MIRA v0.2 pueda construirse con mayor seguridad cuando se empiece a trabajar con archivos CSV y datos climáticos organizados.



Día 4 - Diseño de la arquitectura modular de MIRA v0.2

Fecha: 12 de julio de 2026

Objetivo del día

Definir la arquitectura base de MIRA v0.2, diseñar la estructura modular del proyecto y preparar el repositorio para comenzar el desarrollo de un sistema capaz de procesar archivos CSV de forma organizada.

Durante esta jornada no se implementó todavía la lógica de lectura de datos. El trabajo estuvo enfocado en construir una base sólida sobre la cual desarrollar las próximas funcionalidades de la versión v0.2.

Qué hice

Revisé el alcance previsto para MIRA v0.2 y confirmé que esta versión estará orientada al procesamiento de múltiples registros ambientales almacenados en archivos CSV.

Diseñé la arquitectura general del proyecto, definiendo la responsabilidad de cada módulo y el flujo de datos entre ellos.

Comprendí la diferencia entre un programa compuesto por un único archivo y una arquitectura modular basada en responsabilidades específicas.

Estudié el funcionamiento de las importaciones (import) en Python y cómo permiten que distintos módulos trabajen de forma coordinada.

Analicé el recorrido completo que seguirá un registro ambiental desde que es leído desde un archivo CSV hasta que se convierte en un resultado clasificado.

Definí que la versión v0.2 utilizará un pipeline central encargado de coordinar el procesamiento de los datos.

Se decidió reorganizar el código fuente creando una carpeta específica para la versión:

src/mira_v0_2/

Dentro de esta carpeta quedaron preparados los módulos principales del sistema:

main.py
pipeline.py
io_csv.py
validation.py
risk_engine.py
models.py
config.py

Durante la creación de la estructura surgió un inconveniente al sincronizar el repositorio con GitHub debido a que existían cambios remotos que aún no estaban presentes en la copia local.

Se resolvió correctamente utilizando:

git pull origin main --rebase

Posteriormente se realizó el git push sin conflictos, dejando el repositorio completamente sincronizado.

Arquitectura definida

Se estableció la siguiente organización para MIRA v0.2:

src/
└── mira_v0_2/
    ├── main.py
    ├── pipeline.py
    ├── io_csv.py
    ├── validation.py
    ├── risk_engine.py
    ├── models.py
    └── config.py

Cada módulo tendrá una responsabilidad única:

main.py iniciará la aplicación.
pipeline.py coordinará todo el procesamiento.
io_csv.py realizará la lectura y escritura de archivos CSV.
validation.py validará y convertirá los datos.
risk_engine.py calculará el riesgo ambiental.
models.py contendrá las estructuras de datos.
config.py centralizará reglas, umbrales y configuraciones.
Qué aprendí

Aprendí que un proyecto comienza a crecer cuando cada archivo tiene una responsabilidad específica.

Aprendí que una arquitectura modular hace que el código sea más fácil de mantener, probar y ampliar.

Comprendí que el pipeline no realiza cálculos, sino que coordina el trabajo de los distintos módulos.

Aprendí que las importaciones permiten reutilizar funciones y clases definidas en otros archivos sin duplicar código.

Comprendí la diferencia entre el flujo de control (quién ejecuta cada paso) y el flujo de datos (cómo se transforma la información durante el procesamiento).

Aprendí que Git puede rechazar un push cuando el repositorio remoto contiene cambios que todavía no existen localmente y que esta situación puede resolverse integrando primero los cambios remotos mediante un pull --rebase.

Estado actual

MIRA v0.2 cuenta ahora con una arquitectura modular completamente definida.

La estructura del proyecto quedó preparada para comenzar la implementación de la lectura de archivos CSV y del procesamiento de registros ambientales.

Todavía no existe lógica implementada dentro de los módulos, pero la organización del código quedó establecida y lista para comenzar el desarrollo.

Decisión técnica del día

Se decidió abandonar la idea inicial de concentrar toda la versión v0.2 en un único archivo.

En su lugar, se adoptó una arquitectura basada en módulos especializados agrupados dentro de la carpeta src/mira_v0_2, lo que permitirá mantener el proyecto ordenado y facilitar la incorporación de nuevas funcionalidades en versiones futuras.

También se decidió mantener una separación estricta de responsabilidades para evitar mezclar lectura de datos, validación, cálculos y configuración en un mismo archivo.

Próximos pasos

Implementar la lectura de archivos CSV en io_csv.py.

Crear un archivo CSV de prueba dentro de la carpeta data.

Implementar la validación básica de encabezados.

Construir las estructuras de datos en models.py.

Comenzar el desarrollo del pipeline de procesamiento.

Conclusión del día

Hoy no se incorporaron nuevas funcionalidades visibles al sistema, pero se completó una de las tareas más importantes para el crecimiento del proyecto: definir su arquitectura.

La organización modular permitirá que MIRA evolucione de un programa sencillo hacia un sistema más escalable, donde cada componente tendrá una responsabilidad claramente definida.

Con esta base, la siguiente etapa consistirá en comenzar la implementación del flujo de procesamiento de datos ambientales mediante archivos CSV.
