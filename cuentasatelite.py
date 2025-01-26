import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

# Título del dashboard
st.title("Cuesta Satélite de Cultura SHCP")

# Carga de datos
csv_file = "datos_cultura.csv"
if not os.path.exists(csv_file):
    st.error(f"El archivo '{csv_file}' no se encuentra en la ubicación del programa.")
    st.stop()

try:
    data = pd.read_csv(csv_file, header=None)
except Exception as e:
    st.error(f"Error al leer el archivo CSV: {e}")
    st.stop()

# Procesamiento de datos
try:
    # Extraemos los años (2008-2023)
    anios = list(range(2008, 2024))
    
    # Limpieza y extracción de valores económicos (millones de pesos)
    valores_millones = data.iloc[1:101, 0].apply(lambda x: float(str(x).split('|')[-1].strip()))
    
    # Limpieza y extracción de porcentajes de participación
    participacion_porcentaje = data.iloc[101:201, 0].apply(lambda x: float(str(x).split('|')[-1].strip()))

    # Verificación de tamaños
    if len(valores_millones) != len(anios) or len(participacion_porcentaje) != len(anios):
        st.error("El número de registros no coincide con el rango de años especificado.")
        st.stop()
except Exception as e:
    st.error(f"Error al procesar los datos: {e}")
    st.stop()

# Gráfica 1: Valor económico del sector cultura
st.subheader("Valor económico del sector cultura (millones de pesos)")
fig1, ax1 = plt.subplots()
ax1.plot(anios, valores_millones, marker='o', linestyle='-', color='blue', label='Millones de pesos')
ax1.set_xlabel("Año")
ax1.set_ylabel("Millones de pesos")
ax1.set_title("Evolución del valor económico del sector cultura")
ax1.grid(True)
ax1.legend()
st.pyplot(fig1)

# Gráfica 2: Participación en la economía nacional
st.subheader("Participación del sector cultura en la economía nacional (%)")
fig2, ax2 = plt.subplots()
ax2.bar(anios, participacion_porcentaje, color='green', label='Porcentaje')
ax2.set_xlabel("Año")
ax2.set_ylabel("Porcentaje (%)")
ax2.set_title("Participación del sector cultura en la economía nacional")
ax2.grid(axis='y')
ax2.legend()
st.pyplot(fig2)

# Nota sobre los datos
st.info("Fuente: Datos simulados basados en el archivo proporcionado. Verifica la estructura del CSV antes de usar datos reales.")
