
import pandas as pd
import numpy as np

def cargar_datos(ruta):
    """Carga el dataset desde un archivo Excel."""
    return pd.read_excel(ruta)

def resumen_calidad(df):
    """Entrega información básica sobre la calidad del dataset."""
    return {
        "registros": len(df),
        "columnas": len(df.columns),
        "valores_nulos": int(df.isnull().sum().sum()),
        "duplicados": int(df.duplicated().sum())
    }

def indicadores_red(df):
    """Calcula indicadores principales del monitoreo de la red."""
    return {
        "latencia_promedio_ms": round(np.mean(df["latencia_ms"]), 2),
        "incidencias_promedio": round(np.mean(df["incidencias_reportadas"]), 2),
        "tiempo_resolucion_promedio_hr": round(
            np.mean(df["tiempo_resolucion_hr"]), 2
        ),
        "clientes_afectados_promedio": round(
            np.mean(df["clientes_afectados"]), 2
        )
    }

def latencia_por_region(df):
    """Calcula la latencia promedio para cada región."""
    return (
        df.groupby("region")["latencia_ms"]
        .mean()
        .round(2)
        .sort_values()
    )
