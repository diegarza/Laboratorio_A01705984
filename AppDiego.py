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
st.warning('Warning')
st.error('Error')
st.exception('NameError("no está definido")')
st.header('Obtener información de ayuda de Python')
st.help(range)
st.header('Widgets:')
st.subheader('Checkbox')

if st.checkbox('Show/Hide'):
    st.text('Mostrar u ocultar Widget')
    st.subheader('Radio buttons')
    
status = st.radio('Cuál es tu estatus?', ('Activo','Inactivo'))

if status == 'Activo':
    st.success('Estás activo')
else:
    st.warning('Inactivo')
    st.subheader('Selectbox')

occupation = st.selectbox('Tu ocupación', 
                          ['Programador', 'Científico de datos', 'BI', 'Ingeniero de datos'])
st.write('Opción seleccionada:', occupation)
st.subheader('MultiSelect')

location = st.multiselect('Dónde trabajas?',
                         ('México', 'Nueva York', 'Guadalajara', 'Monterrey', 'Nepal', 'Buenos Aires', 'Caracas'))

st.write('Selección:', len(location), 'locaciones')
st.subheader('Slider')

level = st.slider('Cuál es tu nivel?', 1, 5)
st.write('Nivel:', level)