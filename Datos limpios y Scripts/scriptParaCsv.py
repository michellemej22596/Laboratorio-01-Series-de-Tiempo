import pandas as pd

# Ruta al archivo original
excel_path = "IMPORTACION-HIDROCARBUROS-VOLUMEN-2025-05.xlsx"

# Leer el archivo Excel desde la fila donde empiezan los encabezados reales
df = pd.read_excel(excel_path, sheet_name="IMPORTACION", header=6)

# Eliminar filas completamente vacías
df_clean = df.dropna(how='all')

# Eliminar columnas completamente vacías (opcional, si hay columnas sobrantes)
df_clean = df_clean.dropna(axis=1, how='all')

# Guardar como CSV limpio
df_clean.to_csv("importacion_hidrocarburos_limpio.csv", index=False)

print("CSV limpio guardado como 'importacion_hidrocarburos_limpio.csv'")
