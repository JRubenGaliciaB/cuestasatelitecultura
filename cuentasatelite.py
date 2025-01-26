import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configuración inicial del título
st.set_page_config(page_title="Cuesta Satélite de Cultura SHCP", layout="wide")
st.title("Cuesta Satélite de Cultura SHCP")

# Carga del archivo CSV
st.sidebar.header("Configuración de datos")
csv_file = st.sidebar.file_uploader("Sube el archivo CSV", type="csv")

if csv_file:
    # Leer datos
    df = pd.read_csv(csv_file)

    # Asumir que la primera fila tiene encabezados y se cargan correctamente
    # Encabezado B1 a Q1 son años 2008 a 2023
    df = df.rename(columns={df.columns[0]: "Descriptor"})

    # Opciones disponibles
    descriptors = df["Descriptor"].dropna().unique()
    years = list(df.columns[1:])  # Ignorar la columna Descriptor

    # Selección de filtros
    selected_descriptor = st.sidebar.selectbox("Selecciona un descriptor", descriptors)
    selected_year = st.sidebar.selectbox("Selecciona un año", years)

    # Filtrar datos
    filtered_data = df[df["Descriptor"] == selected_descriptor]
    value = filtered_data[selected_year].values[0]

    # Visualización
    st.subheader(f"Datos seleccionados: {selected_descriptor} en {selected_year}")
    st.metric(label="Valor", value=value)

    # Gráfico
    st.subheader("Comparativa de datos por año")
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(x=years, y=filtered_data.iloc[0, 1:].values, palette="viridis", ax=ax)
    ax.set_title(f"Evolución del descriptor: {selected_descriptor}", fontsize=16)
    ax.set_xlabel("Año", fontsize=14)
    ax.set_ylabel("Valor", fontsize=14)
    st.pyplot(fig)
else:
    st.warning("Por favor, sube un archivo CSV para visualizar los datos.")
