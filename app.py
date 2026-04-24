import streamlit as st
import sqlite3
import random

# ----------------------------
# CREAR BASE DE DATOS
# ----------------------------

conn = sqlite3.connect('usuarios.db', check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios(
usuario TEXT,
password TEXT
)
""")

cursor.execute("SELECT * FROM usuarios WHERE usuario='admin'")
if cursor.fetchone() is None:
    cursor.execute("INSERT INTO usuarios VALUES ('admin','1234')")
    conn.commit()

# ----------------------------
# FUNCION LOGIN
# ----------------------------

def login(usuario, password):

    cursor.execute(
        "SELECT * FROM usuarios WHERE usuario=? AND password=?",
        (usuario, password)
    )

    return cursor.fetchone()


# ----------------------------
# SESION
# ----------------------------

if "logueado" not in st.session_state:
    st.session_state.logueado = False


# ----------------------------
# PANTALLA LOGIN
# ----------------------------

if not st.session_state.logueado:

    st.title("Acceso al Sistema de Casa Inteligente")

    usuario = st.text_input("Usuario")
    password = st.text_input("Contraseña", type="password")

    if st.button("Ingresar"):

        resultado = login(usuario, password)

        if resultado:
            st.session_state.logueado = True
            st.success("Acceso correcto")
            st.rerun()

        else:
            st.error("Usuario o contraseña incorrectos")

# ----------------------------
# PANEL PRINCIPAL
# ----------------------------

else:

    st.title("Panel de Control - Casa Inteligente")

    if "luz" not in st.session_state:
        st.session_state.luz = False

    col1, col2 = st.columns(2)

    # Control luz
    with col1:

        st.subheader("Control de Iluminación")

        if st.session_state.luz:
            st.success("La luz está ENCENDIDA")
        else:
            st.warning("La luz está APAGADA")

        if st.button("Encender / Apagar luz"):
            st.session_state.luz = not st.session_state.luz


    # Sensor temperatura
    with col2:

        st.subheader("Sensor de Temperatura")

        temperatura = random.randint(18, 30)

        st.metric("Temperatura actual", f"{temperatura} °C")

        if temperatura > 27:
            st.error("Temperatura alta")
        else:
            st.info("Temperatura normal")


    # Sensor gas
    st.subheader("⚠ Sensor de Gas")

    gas = random.choice(["Normal", "Fuga detectada"])

    if gas == "Normal":
        st.success("No se detectan fugas de gas")
    else:
        st.error("⚠ ALERTA: Posible fuga de gas detectada")


    # Cámara
    st.subheader("Cámara de Seguridad")

    st.image("camara.jpg")

    st.write("Transmisión simulada de cámara de seguridad en tiempo real.")