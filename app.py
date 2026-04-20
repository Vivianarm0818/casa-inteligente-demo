import streamlit as st
import random

st.set_page_config(page_title="Sistema de Casa Inteligente", layout="wide")

st.title("Panel de Control - Casa Inteligente")

# Inicializar estados
if "luz" not in st.session_state:
    st.session_state.luz = False

# COLUMNAS
col1, col2 = st.columns(2)

# -----------------------------
# MODULO ILUMINACION
# -----------------------------
with col1:
    st.subheader("Control de Iluminación")

    if st.session_state.luz:
        st.success("La luz está ENCENDIDA")
    else:
        st.warning("La luz está APAGADA")

    if st.button("Encender / Apagar luz"):
        st.session_state.luz = not st.session_state.luz


# -----------------------------
# MODULO TEMPERATURA
# -----------------------------
with col2:
    st.subheader("Sensor de Temperatura")

    temperatura = random.randint(18, 30)

    st.metric("Temperatura actual", f"{temperatura} °C")

    if temperatura > 27:
        st.error("Temperatura alta")
    else:
        st.info("Temperatura normal")


# -----------------------------
# SENSOR DE GAS
# -----------------------------
st.subheader("⚠ Sensor de Gas")

gas = random.choice(["Normal", "Fuga detectada"])

if gas == "Normal":
    st.success("No se detectan fugas de gas")
else:
    st.error("⚠ ALERTA: Posible fuga de gas detectada")


# -----------------------------
# CAMARA SIMULADA
# -----------------------------
st.subheader("📷 Cámara de Seguridad")

st.image(
    "https://images.unsplash.com/photo-1581090700227-4c4a6f1a5c3d",
    caption="Vista simulada de cámara de seguridad",
    use_column_width=True
)

st.write("Transmisión simulada de cámara de seguridad en tiempo real.")