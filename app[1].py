import streamlit as st

st.set_page_config(page_title="Mi Observatorio Financiero", page_icon="📈", layout="wide")
st.title("📈 Mi Observatorio Financiero")
st.caption("Laboratorio de aplicaciones financieras · ITM")

st.sidebar.header("⚙️ Configuración")
st.sidebar.write("Aquí elegiremos activos y períodos.")

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Capital de ejemplo", "$10,000")
with col2:
    st.metric("Activos de ejemplo", "3")
with col3:
  st.metric("período de ejemplo", "1")

pestana1, pestana2, pestana3, pestana4, = st.tabs(["📈 Portafolio", "📊 Estadística", "ℹ️ Proyecto", " ⚠️ Riesgo"])
with pestana1:
    st.subheader("Análisis de portafolio")
    st.write("Aquí mostraremos precios y rendimientos.")
with pestana2:
    st.subheader("Estadística descriptiva")
    st.write("Aquí mostraremos media y desviación estándar.")
with pestana3:
    st.subheader("Acerca de mi")
    st.write("Creado con Python y Streamlit.")
with pestana4:
    st.subheader("Información de Riesgo")
    st.write("Aqui mostramos información de riesgo")
