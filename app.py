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

page_style = """
<style>
/* Fondo principal */
[data-testid="stAppViewContainer"] {
    background-color: #5697d5;
}

/* Fondo del sidebar */
[data-testid="stSidebar"] {
    background-color: #9fcefb;
}

/* Color de todos los textos */
[data-testid="stMarkdownContainer"] {
    color: #121314;
}

/* Estilo para los mensajes */
.sentiment-message {
    padding: 10px;
    border-radius: 8px;
    margin: 15px 0;
    font-size: 16px;
    font-weight: bold;
    text-align: center;
}
</style>
"""

st.markdown(page_style, unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.subheader("¿Qué es Polaridad y Subjetividad?")
    st.markdown("""
    **Polaridad:**  
    De -1 (negativo) a 1 (positivo).  
    **Subjetividad:**  
    De 0 (objetivo) a 1 (subjetivo).
    """)

# Mensajes personalizados
MESSAGES = {
    "positive": "¡Tu texto es positivo! 😊 Brilla como el sol ☀️",
    "neutral": "Tu texto es neutral 😐 Como un día nublado ⛅",
    "negative": "Tu texto es negativo 😔 Como la lluvia en lunes 🌧️"
}

# Entrada de texto
with st.expander('🔍 Analizar texto'):
    text1 = st.text_area('✍📜 Escribe tu frase:')
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
            st.markdown(f'<div class="sentiment-message" style="background-color:#d4edda;color:#155724;">{MESSAGES["positive"]}</div>', unsafe_allow_html=True)
            animation = load_lottiefile('positivo.json')
            st_lottie(animation, height=300)
        elif polarity <= -0.5:
            st.markdown(f'<div class="sentiment-message" style="background-color:#f8d7da;color:#721c24;">{MESSAGES["negative"]}</div>', unsafe_allow_html=True)
            animation = load_lottiefile('negativo.json')
            st_lottie(animation, height=300)
        else:
            st.markdown(f'<div class="sentiment-message" style="background-color:#fff3cd;color:#856404;">{MESSAGES["neutral"]}</div>', unsafe_allow_html=True)
            animation = load_lottiefile('neutral.json')
            st_lottie(animation, height=300)

# Corrección de texto en inglés
with st.expander('🛠️ Corrección en Inglés'):
    text2 = st.text_area('✍️📜 Escribe tu texto en inglés:', key='4')
    if text2:
        blob2 = TextBlob(text2)
        st.write('Texto corregido:')
        st.success(blob2.correct())
