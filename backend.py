from sqlalchemy import create_engine
import time
from datetime import datetime
import pandas as pd
import streamlit as st
import pyodbc
import io

@st.cache_data
def convert_df_to_csv(df):
    output = io.BytesIO()  # Create a temporary in-memory file
    df.to_csv(output, index=False, sep=";", decimal=",", encoding='utf-8')  # Write CSV data
    output.seek(0)  # Move cursor to the start
    return output

#RADI!
@st.cache_data
def extract_all_data():
    #if there is some data on the second pressing clear that data
    if "csv_data_download" in st.session_state:
        del st.session_state.csv_data_download 

    with st.spinner(text=" Fetching data...This may take up to a few minutes..."):
        
        server = r"SCADA_POTRESI\WINCC"  # server IP or hostname
        database = "IN23_Plant"  # database name
        username = "remote_login"  # username is added to the SQL Server logins
        password = "1"  # password is for the username that is added in the SQL Server login

        query = """SELECT * FROM [IN23_Plant].[dbo].[General_Table] ORDER BY [Current_Time] ASC"""

        connection_str = f'mssql+pyodbc://{username}:{
            password}@{server}/{database}?driver=SQL+Server'
        
        # Create an SQLAlchemy engine
        engine = create_engine(connection_str)

        if "csv_data_download" not in st.session_state:
            st.session_state.csv_data_download = pd.read_sql(query, engine)
        
        

    st.success('Data has been downloaded successfully!', icon="✅")


#RADI!
def extract_filtered_data_without_date_and_time():
    
    list_of_chosen_data = []
    
    if 'first_group_of_pills' in st.session_state:
        for item in st.session_state.first_group_of_pills:
            list_of_chosen_data.append(item)
    
    if 'second_group_of_pills' in st.session_state:
        for item in st.session_state.second_group_of_pills:
            list_of_chosen_data.append(item)
    
    if 'third_group_of_pills' in st.session_state:
        for item in st.session_state.third_group_of_pills:
            list_of_chosen_data.append(item)
    
    if 'fourth_group_of_pills' in st.session_state:
        for item in st.session_state.fourth_group_of_pills:
            list_of_chosen_data.append(item)
    
    if 'fifth_group_of_pills' in st.session_state:
        for item in st.session_state.fifth_group_of_pills:
            list_of_chosen_data.append(item)
    
    if 'sixth_group_of_pills' in st.session_state:
        for item in st.session_state.sixth_group_of_pills:
            list_of_chosen_data.append(item)
    
    if 'seventh_group_of_pills' in st.session_state:
        for item in st.session_state.seventh_group_of_pills:
            list_of_chosen_data.append(item)
    
    if 'eight_group_of_pills' in st.session_state:
        for item in st.session_state.eight_group_of_pills:
            list_of_chosen_data.append(item)
    
    if 'ninth_group_of_pills' in st.session_state:
        for item in st.session_state.ninth_group_of_pills:
            list_of_chosen_data.append(item)
    
    if 'tenth_group_of_pills' in st.session_state:
        for item in st.session_state.tenth_group_of_pills:
            list_of_chosen_data.append(item)
    
           
    string_for_query = ",".join([f'[{item}]' for item in list_of_chosen_data])
  
    
    
    with st.spinner(text=" Fetching data...This may take up to a few minutes..."):
        
        server = r"SCADA_POTRESI\WINCC"  # server IP or hostname
        database = "IN23_Plant"  # database name
        username = "remote_login"  # username is added to the SQL Server logins
        password = "1"  # password is for the username that is added in the SQL Server login

        query = f"""SELECT [Current_Time],{string_for_query} FROM [IN23_Plant].[dbo].[General_Table] ORDER BY [Current_Time] ASC"""

        connection_str = f'mssql+pyodbc://{username}:{
            password}@{server}/{database}?driver=SQL+Server'
        # Create an SQLAlchemy engine
        engine = create_engine(connection_str)

        # Use pandas to read the SQL query into a DataFrame
        pandas_dataframe = pd.read_sql(query, engine)

    st.success('Data has been downloaded successfully!', icon="✅")

    if "table_data" in st.session_state:
        st.session_state.table_data = pandas_dataframe

#RADI!
@st.cache_data
def extract_data_with_date_and_time():
    
    if "csv_data_download" in st.session_state:
        del st.session_state.csv_data_download 

    with st.spinner(text=" Fetching data...This may take up to a few minutes..."):
        
        server = r"SCADA_POTRESI\WINCC"  # server IP or hostname
        database = "IN23_Plant"  # database name
        username = "remote_login"  # username is added to the SQL Server logins
        password = "1"  # password is for the username that is added in the SQL Server login

        query = f"""SELECT * FROM [IN23_Plant].[dbo].[General_Table]
                    WHERE [Current_Time] >= '{st.session_state.date_from} {st.session_state.time_from}' AND [Current_Time] <= '{st.session_state.date_to} {st.session_state.time_to}'
                    ORDER BY [Current_Time] ASC"""
        
        connection_str = f'mssql+pyodbc://{username}:{
            password}@{server}/{database}?driver=SQL+Server'
        # Create an SQLAlchemy engine
        engine = create_engine(connection_str)

        # Use pandas to read the SQL query into a DataFrame
        pandas_dataframe = pd.read_sql(query, engine)
        
    st.success('Data has been downloaded successfully!', icon="✅")

    if "table_data" in st.session_state:
        st.session_state.table_data = pandas_dataframe
    if "csv_data_download" not in st.session_state:
            st.session_state.csv_data_download = pd.read_sql(query, engine)


#RADI!
def extract_filtered_data_with_date_and_time():
    
    if "csv_data_download" in st.session_state:
        del st.session_state.csv_data_download 

    if st.session_state.get("include_time_and_date_toggle", True):

        list_of_chosen_data = []
        with st.spinner(text=" Fetching data...This may take up to a few minutes..."):
            if 'first_group_of_pills' in st.session_state:
                for item in st.session_state.first_group_of_pills:
                    list_of_chosen_data.append(item)
            
            if 'second_group_of_pills' in st.session_state:
                for item in st.session_state.second_group_of_pills:
                    list_of_chosen_data.append(item)
            
            if 'third_group_of_pills' in st.session_state:
                for item in st.session_state.third_group_of_pills:
                    list_of_chosen_data.append(item)
            
            if 'fourth_group_of_pills' in st.session_state:
                for item in st.session_state.fourth_group_of_pills:
                    list_of_chosen_data.append(item)
            
            if 'fifth_group_of_pills' in st.session_state:
                for item in st.session_state.fifth_group_of_pills:
                    list_of_chosen_data.append(item)
            
            if 'sixth_group_of_pills' in st.session_state:
                for item in st.session_state.sixth_group_of_pills:
                    list_of_chosen_data.append(item)
            
            if 'seventh_group_of_pills' in st.session_state:
                for item in st.session_state.seventh_group_of_pills:
                    list_of_chosen_data.append(item)
            
            if 'eight_group_of_pills' in st.session_state:
                for item in st.session_state.eight_group_of_pills:
                    list_of_chosen_data.append(item)
            
            if 'ninth_group_of_pills' in st.session_state:
                for item in st.session_state.ninth_group_of_pills:
                    list_of_chosen_data.append(item)
            
            if 'tenth_group_of_pills' in st.session_state:
                for item in st.session_state.tenth_group_of_pills:
                    list_of_chosen_data.append(item)
            
                
            string_for_query = ",".join([f'[{item}]' for item in list_of_chosen_data])

            server = r"SCADA_POTRESI\WINCC"  # server IP or hostname
            database = "IN23_Plant"  # database name
            username = "remote_login"  # username is added to the SQL Server logins
            password = "1"  # password is for the username that is added in the SQL Server login

            date_from_for_query = st.session_state.date_from
            time_from_for_query = st.session_state.time_from
            date_to_for_query = st.session_state.date_to
            time_to_for_query = st.session_state.time_to


            query = f"""SELECT {string_for_query} FROM [IN23_Plant].[dbo].[General_Table]
                        WHERE [Current_Time] >= '{date_from_for_query} {time_from_for_query}' AND [Current_Time] <= '{date_to_for_query} {time_to_for_query}'
                        ORDER BY [Current_Time] ASC"""
            
            connection_str = f'mssql+pyodbc://{username}:{
                password}@{server}/{database}?driver=SQL+Server'
            # Create an SQLAlchemy engine
            engine = create_engine(connection_str)

            # Use pandas to read the SQL query into a DataFrame
            pandas_dataframe = pd.read_sql(query, engine)
        
        st.success('Data has been downloaded successfully!', icon="✅")

        if "table_data" in st.session_state:
            st.session_state.table_data = pandas_dataframe
        if "csv_data_download" not in st.session_state:
                st.session_state.csv_data_download = pd.read_sql(query, engine)
        else:
            if "csv_data_download" in st.session_state:
                del st.session_state.csv_data_download 

        with st.spinner(text=" Fetching data...This may take up to a few minutes..."):
        
            server = r"SCADA_POTRESI\WINCC"  # server IP or hostname
            database = "IN23_Plant"  # database name
            username = "remote_login"  # username is added to the SQL Server logins
            password = "1"  # password is for the username that is added in the SQL Server login

            query = f"""SELECT * FROM [IN23_Plant].[dbo].[General_Table]
                        WHERE [Current_Time] >= '{st.session_state.date_from} {st.session_state.time_from}' AND [Current_Time] <= '{st.session_state.date_to} {st.session_state.time_to}'
                        ORDER BY [Current_Time] ASC"""
            
            connection_str = f'mssql+pyodbc://{username}:{
                password}@{server}/{database}?driver=SQL+Server'
            # Create an SQLAlchemy engine
            engine = create_engine(connection_str)

            # Use pandas to read the SQL query into a DataFrame
            pandas_dataframe = pd.read_sql(query, engine)
            
        st.success('Data has been downloaded successfully!', icon="✅")

        if "table_data" in st.session_state:
            st.session_state.table_data = pandas_dataframe
        if "csv_data_download" not in st.session_state:
                st.session_state.csv_data_download = pd.read_sql(query, engine)
        pass
    else:
        list_of_chosen_data = []
    
    if 'first_group_of_pills' in st.session_state:
        for item in st.session_state.first_group_of_pills:
            list_of_chosen_data.append(item)
    
    if 'second_group_of_pills' in st.session_state:
        for item in st.session_state.second_group_of_pills:
            list_of_chosen_data.append(item)
    
    if 'third_group_of_pills' in st.session_state:
        for item in st.session_state.third_group_of_pills:
            list_of_chosen_data.append(item)
    
    if 'fourth_group_of_pills' in st.session_state:
        for item in st.session_state.fourth_group_of_pills:
            list_of_chosen_data.append(item)
    
    if 'fifth_group_of_pills' in st.session_state:
        for item in st.session_state.fifth_group_of_pills:
            list_of_chosen_data.append(item)
    
    if 'sixth_group_of_pills' in st.session_state:
        for item in st.session_state.sixth_group_of_pills:
            list_of_chosen_data.append(item)
    
    if 'seventh_group_of_pills' in st.session_state:
        for item in st.session_state.seventh_group_of_pills:
            list_of_chosen_data.append(item)
    
    if 'eight_group_of_pills' in st.session_state:
        for item in st.session_state.eight_group_of_pills:
            list_of_chosen_data.append(item)
    
    if 'ninth_group_of_pills' in st.session_state:
        for item in st.session_state.ninth_group_of_pills:
            list_of_chosen_data.append(item)
    
    if 'tenth_group_of_pills' in st.session_state:
        for item in st.session_state.tenth_group_of_pills:
            list_of_chosen_data.append(item)
    
           
    string_for_query = ",".join([f'[{item}]' for item in list_of_chosen_data])
  
    
    
    with st.spinner(text=" Fetching data...This may take up to a few minutes..."):
        
        server = r"SCADA_POTRESI\WINCC"  # server IP or hostname
        database = "IN23_Plant"  # database name
        username = "remote_login"  # username is added to the SQL Server logins
        password = "1"  # password is for the username that is added in the SQL Server login

        query = f"""SELECT [Current_Time],{string_for_query} FROM [IN23_Plant].[dbo].[General_Table] ORDER BY [Current_Time] ASC"""

        connection_str = f'mssql+pyodbc://{username}:{
            password}@{server}/{database}?driver=SQL+Server'
        # Create an SQLAlchemy engine
        engine = create_engine(connection_str)

        # Use pandas to read the SQL query into a DataFrame
        pandas_dataframe = pd.read_sql(query, engine)

    st.success('Data has been downloaded successfully!', icon="✅")

    if "table_data" in st.session_state:
        st.session_state.table_data = pandas_dataframe
    
