import numpy as np
import pandas as pd
from pathlib import Path
import re # No se incluye re en requirements.txt porque es un modulo preinstalado de python

ruta_raiz = Path(__file__).resolve().parent.parent
ruta_archivo = ruta_raiz / "data" / "StudentsPerformance.csv"

df = pd.read_csv(ruta_archivo)

print("Data Set Cargado Con Éxito")
print("\n==============\n EXPLORACION INICIAL: \n\n")

# Primeras Filas
print("Primeras filas:")
print(df.head())

# Registros y columnas
filas, columnas = df.shape
print(f"\nDimensiones: {filas} filas y {columnas} columnas")

# Nombres Variables
print("\nVariables en el dataset:")
print(df.columns.tolist())

# Tipos 
print("\nTipos de datos:")
print(df.dtypes)

# Resumen general (combina no nulos, tipos y memoria)
print("\nResumen general:")
df.info()

# Datos nulos:
print("\nValores faltantes por variable:")
print(df.isnull().sum())

# Registros duplicados totales
duplicados = df.duplicated().sum()
print(f"\nRegistros duplicados: {duplicados}")

print("\nEstadísticas variables numéricas:")
print(df.describe())

# Estadísticas variables categóricas / texto
print("\nEstadísticas variables categóricas:")
print(df.describe(include=["object", "category"]))


# === CALIDAD DE LOS DATOS ===
print("\n==== REPORTE DE CALIDAD DE LOS DATOS ====\n")

print("COMPLETITUD")
completitud = (df.notnull().sum() / len(df)) * 100
for columna, porcentaje in completitud.items():
    print(f"{columna}: {porcentaje:.2f}%")

print("\nCONSISTENCIA:")
duplicados = df.duplicated().sum()
print(f"Registros Duplicados: {duplicados}")
print(f"Porcentaje de duplicados: {(duplicados/len(df))*100:.2f}")


# Seccion 2: Promedios (Punto 4 notion)

print("\n====  CALIFICACIÓN PROMEDIO  ====\n")

df["average_score"] = df[
    ["math score", "reading score", "writing score"]
].mean(axis=1)
print(df[["math score", "reading score", "writing score", "average_score"]].head())


print("\n==== CLASIFICACIÓN DEL RENDIMIENTO ACADÉMICO ====\n")
# Criterio:
# - Bajo: < 60 puntos (no aprobatorio o nivel rezagado)
# - Medio: 60 a 79.99 puntos (desempeño regular/bueno)
# - Alto: >= 80 puntos (desempeño sobresaliente)

limites = [0, 59.99, 79.99, 100]
etiquetas = ["Bajo", "Medio", "Alto"]

df["performance_level"] = pd.cut(
    df["average_score"], bins=limites, labels=etiquetas, include_lowest=True
)

conteo_rendimiento = df["performance_level"].value_counts(sort=False)
porcentaje_rendimiento = df["performance_level"].value_counts(
    normalize=True, sort=False
) * 100
tabla_rendimiento = pd.DataFrame(
    {"Total": conteo_rendimiento, "Porcentaje (%)": porcentaje_rendimiento}
)
print(tabla_rendimiento)

# =============
print("\n==== 6. ANÁLISIS DE DATOS ====\n")

# Pregunta 1: ¿Cuál de las tres áreas tiene el promedio más alto?
promedios_materias = df[
    ["math score", "reading score", "writing score"]
].mean()
print("1. Promedio general por asignatura:")
print(promedios_materias.round(2))
print(f"Area más alta: {promedios_materias.idxmax()} ({promedios_materias.max():.2f})")
print(f"Area más baja: {promedios_materias.idxmin()} ({promedios_materias.min():.2f})\n")

# Pregunta 2: ¿Los estudiantes con curso de preparación presentan mejores resultados?
prep_analisis = df.groupby("test preparation course")["average_score"].agg(
    ["count", "mean", "std"]
)
print("2. Impacto del curso de preparación en average_score:")
print(prep_analisis.round(2))
dif_prep = (
    prep_analisis.loc["completed", "mean"] - prep_analisis.loc["none", "mean"]
)
print(f"Diferencia promedio a favor del curso: +{dif_prep:.2f} puntos\n")

# Pregunta 3: ¿Existen diferencias según el nivel educativo de los padres?
padres_analisis = (
    df.groupby("parental level of education")["average_score"]
    .agg(["count", "mean", "median"])
    .sort_values(by="mean", ascending=False)
)
print("3. Rendimiento según nivel educativo parental:")
print(padres_analisis.round(2), "\n")

# Pregunta 4: Rendimiento según tipo de alimentación (lunch) y grupos
almuerzo_analisis = df.groupby("lunch")["average_score"].agg(
    ["count", "mean", "median"]
)
print("4. Rendimiento según tipo de almuerzo:")
print(almuerzo_analisis.round(2), "\n")