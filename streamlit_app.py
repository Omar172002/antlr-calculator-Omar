import streamlit as st
import requests

st.set_page_config(page_title="Calculadora", page_icon="🔢")

# Header con información del estudiante
st.markdown("""
    <div style='text-align: center; padding: 20px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 10px; margin-bottom: 30px;'>
        <h1 style='color: white; margin: 0;'> Calculadora</h1>
        <p style='color: white; margin: 10px 0 0 0; font-size: 16px;'>
            Omar Arias Zepeda | A00830966
        </p>
    </div>
""", unsafe_allow_html=True)

# Input con estilo
st.markdown("### Ingresa tu expresión matemática")
expression = st.text_input('', placeholder='Ejemplo: 2+3*8', label_visibility='collapsed')

# Botón centrado
col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    button = st.button(' Calcular', use_container_width=True)

# Resultado
if button:
    if expression:
        response = requests.post(
            'https://antlr-calculator-api-706l.onrender.com/calc',
            json={'statement': expression}
        )
        result = response.json()
        
        st.markdown("---")
        st.markdown("### Resultado")
        st.success(f"# {result['result']}")
    else:
        st.warning(' Por favor ingresa una expresión')
