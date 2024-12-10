import streamlit as st
import pandas as pd
from PIL import Image
# from tensorflow.keras.models import load_model
# modelCNN = load_model('/content/mi_modelo.keras')

dictLabelY_en = {
    'Juice' : 0,
    'Milk' : 1,
    'Oat-Milk' : 2,
    'Oatghurt' : 3,
    'Sour-Cream' : 4,
    'Sour-Milk' : 5,
    'Soy-Milk' : 6,
    'Soyghurt' : 7,
    'Yoghurt' : 8
    }


dictLabelY_es = {
    'Jugo' : 0,
    'Leche' : 1,
    'Leche de avena' : 2,
    'Yogur de avena' : 3,
    'Crema agria' : 4,
    'Leche agria' : 5,
    'Leche de soja' : 6,
    'Yogur de soja' : 7,
    'Yogur' : 8
    }

data = {
    'Producto': [
        'Jugo',
        'Leche',
        'Leche de avena',
        'Yogur de avena',
        'Crema agria',
        'Leche agria',
        'Leche de soja',
        'Yogur de soja',
        'Yogur'
    ],
    'Probabilidad': [
        1.443800e-03,
        9.953145e-01,
        9.683145e-08,
        4.080133e-04,
        3.624214e-05,
        8.790812e-08,
        8.296442e-06,
        1.299992e-06,
        2.787615e-03
    ]
}

# Crear el DataFrame
data = pd.DataFrame(data)


# Título de la aplicación
st.title("Aplicación de Clasificación de Imágenes de Productos")

# Sección para cargar un archivo de imagen
uploaded_file = st.file_uploader("Elige una imagen", type=["jpg", "jpeg", "png"])

# Agregar una línea fina como separador
st.markdown("---")  # Esta línea crea una línea horizontal

# Crear dos columnas
col1, col2 = st.columns(2)

if uploaded_file is not None:
    # Abrir la imagen
    image = Image.open(uploaded_file)
    
    # Mostrar la imagen en la primera columna
    with col1:
        st.image(image, caption='Imagen Cargada', use_container_width=True)

    # Caja informativa en la segunda columna
    with col2:
        st.metric(label="Categoría: Leche (Milk)", value=0.9953145)  # Cambia el valor según sea necesario
        
        st.table(data)  # Mostrar la tabla

# Instrucciones para el usuario
st.write("Sube una imagen para ver su visualización y más información.")