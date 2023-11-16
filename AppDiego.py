import datetime
import time
import pandas as pd
import streamlit as st
from PIL import Image

st.title('Título: Analítica de Datos')

st.header('Este es un header')
st.subheader('Este es un subheader')

st.text('Texto: Hola Streamlit!')
st.markdown('#Este es un markdown h1 \n ##Este es un h2 \n ###Este es un h3')
st.header('Colores de texto y mensajes de error')
st.info('Información!')
st.warning('Warninf')
st.error('Errpr')
st.exception('NameError("no está definido")')
st.header('Obtener información de ayuda de Python')
st.help(range)
st.header('Widgets:')
st.subheader('Checkbox')