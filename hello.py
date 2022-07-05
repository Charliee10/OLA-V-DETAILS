from gettext import find
from click import option
from numpy import choose
import pandas as pd
#import streamlit as st
#import plotly.express as px
import altair as alt
import pandas as pd
#import matplotlib.pyplot as plt
#import plotly.graph_objects as go
#from plotly.subplots import make_subplots
from PIL import Image
import streamlit as st
from streamlit_option_menu import option_menu




#Pagesetup
base="light"
st.set_page_config(page_title='VEHICLE DETAILS', layout = "wide")
st.header('FUTURE FACTORY:CREATING FUTURE')
hide_St_style = """
                <style>
                MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                </style>
                """
image = Image.open('C:\\Users\\akhil.ajayaghosh\\Documents\\logo.jpg')
st.image(image, use_column_width=True)

st.markdown(hide_St_style, unsafe_allow_html=True)
#st.subheader('VEHICLE DETAILS')

#Sidebar Information
#st.sidebar.subheader('vin no:')
#st.sidebar.info('Enter the vin to be checked')
#title = st.text_input('VIN NUMBER', 'Eg: P53AFDCB8BBA09313')

#Sidebar file upload
uploaded_file = st.sidebar.file_uploader(
                    label="UPLOAD MASTER FILE.", 
                    type=['csv'])
#CSV Uploader

global df

if uploaded_file is not None:
    print(uploaded_file)
    print('File uploaded')
    try:
        df = pd.read_csv(uploaded_file)
    except Exception as e:
        print(e)

#Changing all data to 'float' datatype
global numeric_columns
try:
    numeric_columns = list(df.select_dtypes('float').columns)  
except Exception as e:
    print(e)
    #st.write("Upload your csv file") 

with st.sidebar:
    selected = option_menu(menu_title = None ,options = ['ola','vin details'],)

if selected == 'ola':
    st.title('whatever you seek may find you ')


if selected == 'vin details':
    title = st.text_input('VIN NUMBER', 'Eg: P53AFDCB8BBA09313')


    st.subheader('VEHICLE DETAILS')
    if st.button('ENTER'):

        #st.write('Good Morning') #displayed when the button is clicked

        a=title

        st.write((df.loc[df['VIN NO'].str.contains(a)]) )

   # else:

        #st.write('Have a great day') #displayed when the button is unclicked

    #a=title
    #st.write((df.loc[df['VIN NO'].str.contains(a)]) )
    

   
