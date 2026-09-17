import numpy as np
import pandas as pd
from pathlib import Path

ruta_raiz = Path(__file__).resolve().parent.parent
ruta_archivo = ruta_raiz / "data" / "archivo.csv"

df = pd.read_csv(ruta_archivo)

print("Data Set Cargado Con Éxito")