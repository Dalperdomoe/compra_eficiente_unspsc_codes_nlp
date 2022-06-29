import streamlit as st
import pandas as pd
from PIL import Image
def cabecera():
    st.title("Colombia Compra Eficiente")

def imagen():
    image = Image.open('colombiaCompra.png')
    st.image(image, caption='Colombia Compra Eficiente')
def botoncito():
    # Cargar el Archivo
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        # Lectura del Archivo
        #st.write("filename:", uploaded_file.name)
        st.subheader('Validation Table')
        df1 = pd.read_excel(uploaded_file)
        st.dataframe(df1)
        st.markdown('A validation table is shown with the complete results of the classification.'
                    ' It gives you a suggestion to change your **UNSPC** code or a recommendation'
                    ' for your contract ')
        st.subheader('Words Count')
        image = Image.open('servicios.png')
        st.image(image, caption='Colombia Compra Eficiente')
        # Grafica
        #g = df1['Sale Price']
        #st.line_chart(g)


            #bytes_data = uploaded_file.read()
            #st.write("filename:", uploaded_file.name)
            #st.write(bytes_data)
            #st.write('Buena may')
            #data = {'Contract number':[123456, 24561012, 369121518, 48121620, 510152025],
            #        'Contract Type': ['Food', 'Integral Services', 'Construction materials', 'Health', 'Others'],
            #        'Probability': [0.99, 0.97, 0.94, 0.90, 0.85]}
            #df = pd.DataFrame(data)

def codigoSugerido():
    st.header('Analysis results')
    #st.text('10101501')  
    #st.text('90%') 
    st.subheader('10101501')
    st.subheader('90%')

    st.subheader('Classification')

    #st.table(columns= )

    df = pd.DataFrame(
    columns=('Percentage', 'Category', 'Detail')
    )

    row1 = ['70%', 'Segment', '10- Live Plant and Animal']
    row2 = ['90%', 'Family', '10- Live Animals']
    row3 = ['60%', 'Class', '15- Livestock']
    row4 = ['80%', 'Commodity', '01- Cats']

    df = df.append(pd.Series(row1, index=df.columns[:len(row1)]), ignore_index=True)
    df = df.append(pd.Series(row2, index=df.columns[:len(row2)]), ignore_index=True)
    df = df.append(pd.Series(row3, index=df.columns[:len(row3)]), ignore_index=True)
    df = df.append(pd.Series(row4, index=df.columns[:len(row4)]), ignore_index=True)

    st.table(df)

def top3():
    st.subheader('Top 3: Other Sugested UNPSC codes ')
    df = pd.DataFrame(
    columns=('Percentage', 'Code')
    )

    row1 = ['86%', '10101502']
    row2 = ['30%', '44121902']
    row3 = ['15%', '44121803']

    df = df.append(pd.Series(row1, index=df.columns[:len(row1)]), ignore_index=True)
    df = df.append(pd.Series(row2, index=df.columns[:len(row2)]), ignore_index=True)
    df = df.append(pd.Series(row3, index=df.columns[:len(row3)]), ignore_index=True)

    st.table(df)


imagen()
cabecera()
botoncito()
codigoSugerido()
top3()

