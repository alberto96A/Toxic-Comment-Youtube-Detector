import streamlit as st


def YT_logo():
    html_code = """
    <div style="display: flex; align-items: center; justify-content: center;">
        <div style="background-image: url('https://www.freeiconspng.com/uploads/youtube-play-icon-png-0.png');
                    background-size: cover;
                    height: 80px;
                    width: 80px;">
        </div>
        <span style="font-size: 24px; font-weight: bold; margin-left: 10px; color: black;">Toxic </span>
        <span style="font-size: 24px; font-weight: bold; margin-left: 10px; color: white;">Comment Detector</span>
    </div>
    """

    return html_code


# Usar la función en tu aplicación
st.markdown(YT_logo(), unsafe_allow_html=True)

# Añadir el botón
if st.button("¿Qué video quieres examinar? ¡Introduce aquí abajo la URL y lo descubriremos rápidamente!"):
    # Redirigir a otra página (survey.py en este caso)
    st.experimental_set_query_params(my_page="survey")
    st.markdown("<script>window.location.href = window.location.href;</script>",
                unsafe_allow_html=True)

    # Espacio en blanco para insertar cualquier URL de YouTube
    url_input = st.text_input("Inserta la URL de YouTube aquí:")

# Lógica de redirección basada en parámetros de consulta
if "my_page" in st.experimental_get_query_params():
    if st.experimental_get_query_params()["my_page"] == "survey":
        # Contenido de survey.py
        st.write("¡Bienvenido a la página de encuestas!")
