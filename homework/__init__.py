import os
import pandas as pd
import matplotlib.pyplot as plt

# Crear carpetas necesarias
os.makedirs("files/output", exist_ok=True)
os.makedirs("files/plots", exist_ok=True)

# Cargar archivos
drivers = pd.read_csv("files/input/drivers.csv")
timesheet = pd.read_csv("files/input/timesheet.csv")

# Sumar horas y millas por conductor
sum_timesheet = timesheet.groupby("driverId")[["hours-logged", "miles-logged"]].sum().reset_index()

# Unir con nombres de conductores
summary = pd.merge(sum_timesheet, drivers[["driverId", "name"]], on="driverId")

# Guardar el archivo summary.csv
summary.to_csv("files/output/summary.csv", index=False)

# Seleccionar top 10 por millas
top10 = summary.sort_values(by="miles-logged", ascending=False).head(10)

# Crear gráfico
plt.figure(figsize=(10, 6))
plt.barh(top10["name"], top10["miles-logged"], color='skyblue')
plt.xlabel("Millas Registradas")
plt.ylabel("Nombre del Conductor")
plt.title("Top 10 Conductores por Millas Registradas")
plt.gca().invert_yaxis()
plt.tight_layout()

# Guardar imagen
plt.savefig("files/plots/top10_drivers.png")

