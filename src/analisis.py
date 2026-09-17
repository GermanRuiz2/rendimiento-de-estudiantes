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
