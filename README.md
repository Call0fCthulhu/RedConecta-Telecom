# Proyecto de análisis - RedConecta Telecom S.A.

## Objetivo

Analizar la información operacional de RedConecta Telecom S.A. para identificar diferencias en el desempeño del servicio y generar información que apoye la toma de decisiones relacionadas con la calidad del servicio, soporte técnico y experiencia de clientes.

## Etapas del análisis

1. Carga del dataset de telecomunicaciones mediante Python y Pandas.
2. Revisión de dimensiones, variables y tipos de datos.
3. Verificación de valores nulos, registros duplicados y consistencia de variables categóricas.
4. Análisis estadístico descriptivo de las variables numéricas.
5. Análisis de latencia promedio por región.
6. Análisis de incidencias promedio por tipo de servicio.
7. Análisis del tiempo promedio de resolución por región.
8. Revisión del cumplimiento del SLA.
9. Construcción de un dashboard exploratorio.
10. Análisis de correlaciones entre variables operacionales.
11. Generación de archivos para Soporte Técnico y Experiencia de Clientes.
12. Control de versiones mediante Git y respaldo de los archivos del proyecto.

## Principales resultados

- El dataset contiene 200 registros y 10 variables.
- No se detectaron valores nulos ni registros duplicados.
- La región Centro presentó la mayor latencia promedio, con 68.06 ms.
- Internet Hogar presentó el mayor promedio de incidencias, con 14.09.
- La región Sur presentó el mayor tiempo promedio de resolución, con 28.20 horas.
- Se registraron 104 casos que no cumplen el SLA y 96 que sí cumplen.
- No se observaron correlaciones lineales fuertes entre las variables numéricas analizadas.

## Archivos generados

- dataset_set_D_telecomunicaciones.xlsx
- reporte_soporte_tecnico.csv
- reporte_experiencia_clientes.csv

## Herramientas utilizadas

- Python
- Pandas
- Matplotlib
- Google Colab
- Git
- Google Drive

## Reutilización

El proyecto fue organizado para que el análisis pueda volver a ejecutarse cuando se incorporen nuevos datos. Manteniendo la misma estructura de variables, es posible actualizar el dataset y ejecutar nuevamente el flujo para obtener indicadores, visualizaciones y reportes actualizados.
