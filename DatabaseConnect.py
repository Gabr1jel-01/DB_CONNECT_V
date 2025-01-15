import backend
import streamlit as st
import numpy as np
import plotly.express as px
from datetime import datetime
import pandas as pd
import time 
import pyodbc

st.markdown(
    """
    <style>
    .block-container {
        padding-top: 2.8rem;
        padding-right: 2rem;
        padding-left: 2rem;
        max-width: 90%;
        margin-left: auto;
        margin-right: auto;
    }
    </style>
    """,
    unsafe_allow_html=True
)

    
if "date_from" not in st.session_state:
    st.session_state.date_from = None
if "date_to" not in st.session_state:
    st.session_state.date_to = None
if "time_from" not in st.session_state:
    st.session_state.time_from = None
if "time_to" not in st.session_state:
    st.session_state.time_to = None


@st.cache_data
def display_file_in_a_table(data_to_be_displayed):
    st.dataframe(data_to_be_displayed)

with st.sidebar:
    
    st.title("File:")
    file_uploader_dragNdrop = st.file_uploader("Choose a file to upload:")
    st.divider()
    st.subheader("To download the latest table of readings simply click the :red[GET LATEST READINGS] button below")
    button_get_latest_readings = st.button("GET LATEST READINGS", type="primary", on_click=backend.data_extraction)
    
    st.divider()
    #endregion


    #region DOWNLOAD CUSTOM TIME AND DATE FROM THE TABLE
    st.subheader("To download specific table of readings you need to choose the date and time:")
    first_column, second_column = st.columns(2)
    with first_column:
        date_input_date_picker_from = st.date_input("From",
                                                format="DD-MM-YYYY",
                                                key="date_from",
                                                value=st.session_state.date_from)



        date_input_date_picker_to = st.date_input("To",
                                            format="DD-MM-YYYY",
                                            key="date_to",
                                            value=None)

        
    with second_column:
        time_input_time_picker_from = st.time_input("From:",
                                                key="time_from",
                                                value=None)
                                                

        time_input_time_picker_to = st.time_input("To:",
                                                key="time_to",
                                                value=None)

    button_download = st.button("DOWNLOAD", type="primary")    


    st.divider()
    #endregion

    st.write(st.session_state)

if file_uploader_dragNdrop is not None:
    dataframe = pd.read_csv(file_uploader_dragNdrop)
    st.header("Line chart of selected data:")
    df = pd.DataFrame({
                        'x': range(10000),
                        'y1': [i * 2 for i in range(10000)],
                        'y2': [i * 3 for i in range(10000)],
                        'y3': [i * 4 for i in range(10000)]})
    # Reshape the DataFrame to long format         
    df_melted = pd.melt(df, id_vars=['x'],var_name='variable', value_name='value')
    # Create the line chart        
    fig = px.line(         
        df_melted,         
        x='x',         
        y='value',         
        color='variable',  # Different lines for each variable
    )
    st.plotly_chart(fig)
    st.divider()  
    st.header("Table of loaded file:")
    display_file_in_a_table(dataframe)
        
else:
        st.warning('To start, please load a file', icon="⚠️")
