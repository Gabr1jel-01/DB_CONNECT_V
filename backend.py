from sqlalchemy import create_engine
import time
from datetime import datetime
import pandas as pd
import streamlit as st
import pyodbc



#primam string varijablu u data extractions
def extract_all_data():
    with st.spinner(text=" Fetching data...This may take up to a few minutes..."):
        
        server = r"SCADA_POTRESI\WINCC"  # server IP or hostname
        database = "IN23_Plant"  # database name
        username = "remote_login"  # username is added to the SQL Server logins
        password = "1"  # password is for the username that is added in the SQL Server login

        query = """SELECT * FROM [IN23_Plant].[dbo].[General_Table] ORDER BY [Current_Time] ASC"""
        print("Query created")
        print()

        connection_str = f'mssql+pyodbc://{username}:{
            password}@{server}/{database}?driver=SQL+Server'

        
        # Create an SQLAlchemy engine
        engine = create_engine(connection_str)
        # Use pandas to read the SQL query into a DataFrame
        dataframe = pd.read_sql(query, engine)
        # Save the DataFrame to an Excel file
        csv_data = dataframe.to_csv(index=False, sep=";", decimal=",")
        st.session_state.download_csv = csv_data

    st.success('Data has been downloaded successfully!', icon="✅")



@st.cache_data
def extract_specific_data_withouth_date_and_time():
    
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
        print("Query created")
        print()
        
        connection_str = f'mssql+pyodbc://{username}:{
            password}@{server}/{database}?driver=SQL+Server'
        """
        connection_str = pymssql.connect(
            server="SCADA_POTRESI\WINCC",
            user="remote_login",
            password="1",
            database="IN23_Plant")
        """
        # Create an SQLAlchemy engine
        engine = create_engine(connection_str)

        # Use pandas to read the SQL query into a DataFrame
        pandas_dataframe = pd.read_sql(query, engine)
        
            
            
        """
            # Save the DataFrame to an Excel file
            dataframe.to_csv('Reading' + f"{date_for_file_name}.csv", index=False, sep=";", decimal=",")
            print("Writing data to a CSV file...")
            print("Data has been successfully written to 'table.csv'!")
            
            
            print()
            print("Time it took to finish the reading:", time_of_execution)
            print()
            print("Time it took to connect to the database:", time_of_engine_creation)
            print()
            print("Time it took to get the data:", time_of_pdread_creation)
            print()
        """
            

        

    #st.success('Data has been downloaded successfully!', icon="✅")

    if "table_data" in st.session_state:
        st.session_state.table_data = pandas_dataframe
    

def extract_specific_data_with_date_and_time():
    pass


    
    
    


    

    

    
