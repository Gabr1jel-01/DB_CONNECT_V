from sqlalchemy import create_engine
import time
from datetime import datetime
import pandas as pd
import streamlit as st





def data_extraction():
    with st.spinner(text="Fetching data...This may take up to a few minutes..."):
        
        server = r"SCADA_POTRESI\WINCC"  # server IP or hostname
        database = "IN23_Plant"  # database name
        username = "remote_login"  # username is added to the SQL Server logins
        password = "1"  # password is for the username that is added in the SQL Server login

        query = """SELECT * FROM [IN23_Plant].[dbo].[General_Table] ORDER BY [Current_Time] ASC"""
        print("Query created")
        print()

        connection_str = f'mssql+pyodbc://{username}:{
            password}@{server}/{database}?driver=SQL+Server'

        date_for_file_name = datetime.now().strftime("%d%m%Y")

        starting_time = datetime.now()
        starting_time.strftime("%H:%M:%S")
        try:
            # Create an SQLAlchemy engine
            engine = create_engine(connection_str)

            time_to_engine = datetime.now()
            time_to_engine.strftime("%H:%M:%S")

            time.sleep(1)
            print("Reading Data...")
            # Use pandas to read the SQL query into a DataFrame
            print("Connection Successful...")
            dataframe = pd.read_sql(query, engine)
            time_from_pdread = datetime.now()
            time_from_pdread.strftime("%Y%m%d%H%M")

            # Save the DataFrame to an Excel file
            dataframe.to_csv('Reading' + f"{date_for_file_name}.csv", index=False, sep=";", decimal=",")
            print("Writing data to a CSV file...")
            print("Data has been successfully written to 'table.csv'!")
            finish_time = datetime.now()
            finish_time.strftime("%H:%M:%S")
            time_of_execution = finish_time - starting_time
            time_of_engine_creation = time_to_engine - starting_time
            time_of_pdread_creation = time_from_pdread - starting_time
            print()
            print("Time it took to finish the reading:", time_of_execution)
            print()
            print("Time it took to connect to the database:", time_of_engine_creation)
            print()
            print("Time it took to get the data:", time_of_pdread_creation)
            print()
            

        except Exception as e:
            print("Error:", e)

    st.success('Data has been downloaded successfully!', icon="✅")

   

def specific_data_extraction():
    
    with st.spinner(text="Fetching data...This may take up to a few minutes..."):
        
        server = r"SCADA_POTRESI\WINCC"  # server IP or hostname
        database = "IN23_Plant"  # database name
        username = "remote_login"  # username is added to the SQL Server logins
        password = "1"  # password is for the username that is added in the SQL Server login

        query = """ SELECT *
                    FROM [IN23_Plant].[dbo].[General_Table]
                    WHERE Current_Time BETWEEN 'YYYY-MM-DD HH:MM' AND 'YYYY-MM-DD HH:MM';"""
        print("Query created")
        print()

        connection_str = f'mssql+pyodbc://{username}:{
            password}@{server}/{database}?driver=SQL+Server'

        date_for_file_name = datetime.now().strftime("%d%m%Y")

        starting_time = datetime.now()
        starting_time.strftime("%H:%M:%S")
        try:
            # Create an SQLAlchemy engine
            engine = create_engine(connection_str)

            time_to_engine = datetime.now()
            time_to_engine.strftime("%H:%M:%S")

            time.sleep(1)
            print("Reading Data...")
            # Use pandas to read the SQL query into a DataFrame
            print("Connection Successful...")
            dataframe = pd.read_sql(query, engine)
            time_from_pdread = datetime.now()
            time_from_pdread.strftime("%Y%m%d%H%M")

            # Save the DataFrame to an Excel file
            dataframe.to_csv('Reading' + f"{date_for_file_name}.csv", index=False, sep=";", decimal=",")
            print("Writing data to a CSV file...")
            print("Data has been successfully written to 'table.csv'!")
            finish_time = datetime.now()
            finish_time.strftime("%H:%M:%S")
            time_of_execution = finish_time - starting_time
            time_of_engine_creation = time_to_engine - starting_time
            time_of_pdread_creation = time_from_pdread - starting_time
            print()
            print("Time it took to finish the reading:", time_of_execution)
            print()
            print("Time it took to connect to the database:", time_of_engine_creation)
            print()
            print("Time it took to get the data:", time_of_pdread_creation)
            print()
            

        except Exception as e:
            print("Error:", e)

    st.success('Data has been downloaded successfully!', icon="✅")
    
    pass

    
    
