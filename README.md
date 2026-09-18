# Análisis de Promedios respecto a Diversos Factores  
Este proyecto genera un análisis de los promedios de estudiantes de una escuela, según diferentes categorías, tales como su grupo étnico, tipo de lunch, y un analisis respecto al nivel de educación previo de los padres.

Para esto se utiliza el siguiente dataset, presentado en el folder data.
**Students Performance in Exams**
Extraída de: _https://www.kaggle.com/datasets/spscientist/students-performance-in-exams/data_
Descripción: Notas aseguradas de los estudiantes de una preparatoria en Estados Unidos, con información respecto a sus promedios, grupos étnicos, tipo de lunch, y preparación para el examen, así como también la preparación de los padres en cuestión de educación.

## Objetivo:
Se pretende analizar una estadistica descriptiva, promedios, medianas, para averiguar en promedio quienes son los mejores estudiantes, y si hay alguna relación con que pertenezcan a un grupo étnico, tengan cierto tipo de lunch, o sus padres tengan titulo universitario.

## Requisitos:

Se requiere una versión estable de **Python 3** y la instalación de todas las librerías incluidas en [requirements.txt](requirements.txt)

## Instalación:
Clonar el repositorio localmente:
 ```bash
   git clone https://github.com/GermanRuiz2/rendimiento-de-estudiantes
   ```
Entrar al proyecto:
 ```bash
   cd rendimiento-de-estudiantes
   ```

Crea un entorno virtual:
 ```bash
   python -m venv .venv
   ```
Activa el entorno virtual:
```bash
   .venv\Scripts\Activate.ps1
   ```
Instalar dependencias de requirements.txt:
 ```bash
   pip install -r requirements.txt
   ```

## Ejecución
Una vez instalado el repositorio y dependencias, procede a moverte a la carpeta del proyecto
 ```bash
   cd rendimiento-de-estudiantes
   ```
Y ejecuta el siguiente comando para ejecutar el script de analisis:
 ```bash
   python src/analisis.py
   ```

## Analisis Realizados:
Se realizaron analisis estadísticos exploratorios, validando primero la completitud y consistencia de los datos, también se valida que no haya datos nulos.
Se realiza una impresión de los tipos de datos que maneja el dataset, y de las entradas totales así como las columnas o variables que existen en este mismo.
Como resultados, se muestran los promedios generales de las calificaciones, según cada factor mencionado anteriormente.
En consola, se presentan todos los datos estadísticos para estos factores, sin embargo, se graficaron las 3 con más movimiento posible.

## Conclusiones:
Las habilidades de comprensión y expresión escrita dominan el rendimiento general: Lectura lidera con un promedio de 69.17 puntos, seguida de cerca por Escritura (68.05 puntos).

Los alumnos que completaron el curso obtuvieron un promedio global de 72.67 puntos, en comparación con 65.04 puntos del grupo sin preparación

El rendimiento de los alumnos mantiene una relación proporcional directa con el nivel educativo alcanzado por sus padres:

Nivel máximo: Padres con maestría (master's degree) obtienen un promedio filial de 73.60 puntos.

Nivel intermedio: Padres con una licenciatura (bachelor's degree) o un grado de asociado (el associate's degree) promedian 71.92 y 69.57 puntos, respectivamente.

Nivel inferior: Aquellos cuyos padres solo cursaron bachillerato (high school) registraron el promedio más rezagado (63.10 puntos, más de 10 puntos de diferencia respecto a posgrado).

La variable lunch evidencia una de las mayores disparidades del estudio: los alumnos con régimen alimentario estándar alcanzaron una media global de 70.84 puntos, frente a 62.20 puntos de aquellos bajo subsidio (free/reduced).

En conclusión, el exito escolar en este conjunto de datos está como tal fuertemente modulado por los cursos de preparación, y los factores de contexto (apoyo familiar consolidado y estabilidad económica/nutricional), los cuales explican la mayor parte de la dispersión en las calificaciones.
