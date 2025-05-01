import streamlit as st
from textblob import TextBlob
from googletrans import Translator
from streamlit_lottie import st_lottie
import json

# Función para cargar animaciones desde archivo JSON
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

# Traductor
translator = Translator()

# Título
st.set_page_config(page_title="Análisis de Sentimiento", page_icon="💬", layout="centered")
st.title('💬 Analizador de Sentimiento con Animaciones')

page_bg_color = """
<style>
/* Fondo principal */
[data-testid="stAppViewContainer"] {
    background-color: #d3f8e3; /* Cambia el color de la página principal */
}

/* Fondo del sidebar */
[data-testid="stSidebar"] {
    background-image: url("https://img.freepik.com/free-vector/simple-pattern-background_1319-147.jpg");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;

[data-testid="stMarkdownContainer"] {
    color: #0e0f15;
}
</style>
"""

st.markdown(page_bg_color, unsafe_allow_html=True)



# Sidebar
with st.sidebar:
    st.subheader("¿Qué es Polaridad y Subjetividad?")
    st.markdown("""
    **Polaridad:**  
    De -1 (negativo) a 1 (positivo).  
    **Subjetividad:**  
    De 0 (objetivo) a 1 (subjetivo).
    """)

# Entrada de texto
with st.expander('🔍 Analizar texto'):
    text1 = st.text_area('✍️ Escribe tu frase:')
    if text1:
        # Traducir de español a inglés
        translation = translator.translate(text1, src="es", dest="en")
        trans_text = translation.text
        blob = TextBlob(trans_text)

        # Resultados
        polarity = round(blob.sentiment.polarity, 2)
        subjectivity = round(blob.sentiment.subjectivity, 2)
        st.write('**Polaridad:**', polarity)
        st.write('**Subjetividad:**', subjectivity)

        # Mostrar interacción según el sentimiento
        if polarity >= 0.5:
            st.success('¡Sentimiento Positivo! 😊')
            animation = load_lottiefile('positivo.json')
            st_lottie(animation, height=300)
        elif polarity <= -0.5:
            st.error('Sentimiento Negativo 😔')
            animation = load_lottiefile('negativo.json')
            st_lottie(animation, height=300)
        else:
            st.warning('Sentimiento Neutral 😐')
            animation = load_lottiefile('neutral.json')
            st_lottie(animation, height=300)

# Corrección de texto en inglés
with st.expander('🛠️ Corrección en Inglés'):
    text2 = st.text_area('✍️ Escribe tu texto en inglés:', key='4')
    if text2:
        blob2 = TextBlob(text2)
        st.write('Texto corregido:')
        st.success(blob2.correct())
