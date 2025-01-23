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

# ove globalne varijable mozda necu morati koristiti
CHOSEN_PILLS = []

SPECIFIC_DATE_FROM = ""
SPECIFIC_TIME_FROM = ""
SPECIFIC_DATE_TO = ""
SPECIFIC_TIME_TO = ""

SPECIFIC_QUERY = ""


    
if "date_from" not in st.session_state:
    st.session_state.date_from = None
if "date_to" not in st.session_state:
    st.session_state.date_to = None
if "time_from" not in st.session_state:
    st.session_state.time_from = None
if "time_to" not in st.session_state:
    st.session_state.time_to = None



def reset_filters():

    if "time_to" in st.session_state:
        st.session_state.time_to = None
    if "time_from" in st.session_state:
        st.session_state.time_from = None
    if "date_to" in st.session_state:
        st.session_state.date_to = None
    if "date_from" in st.session_state:
        st.session_state.date_from = None



    if "first_group_of_pills" in st.session_state:
        st.session_state.first_group_of_pills = []
    else:
        pass
    if "second_group_of_pills" in st.session_state:
        st.session_state.second_group_of_pills = []
    else:
        pass
    if "third_group_of_pills" in st.session_state:
        st.session_state.third_group_of_pills = []
    else:
        pass
    if "fourth_group_of_pills" in st.session_state:
        st.session_state.fourth_group_of_pills = []
    else:
        pass
    if "fifth_group_of_pills" in st.session_state:
        st.session_state.fifth_group_of_pills = []
    else:
        pass
    if "sixth_group_of_pills" in st.session_state:
        st.session_state.sixth_group_of_pills = []
    else:
        pass
    if "seventh_group_of_pills" in st.session_state:
        st.session_state.seventh_group_of_pills = []
    else:
        pass
    if "eight_group_of_pills" in st.session_state:
        st.session_state.eight_group_of_pills = []
    else:
        pass
    if "ninth_group_of_pills" in st.session_state:
        st.session_state.ninth_group_of_pills = []
    else:
        pass
    if "tenth_group_of_pills" in st.session_state:
        st.session_state.tenth_group_of_pills = []
    else:
        pass
    if "dataframe" in st.session_state:
        st.session_state.dataframe = None

# ovo mozda necu trebati koristiti
def append_date_from():
    SPECIFIC_DATE_FROM = st.session_state.date_from
    print(SPECIFIC_DATE_FROM)

def append_time_from():
    SPECIFIC_TIME_FROM = st.session_state.time_from
    print(SPECIFIC_TIME_FROM)

def append_date_to():
    SPECIFIC_DATE_TO = st.session_state.date_to
    print(SPECIFIC_DATE_TO)

def append_time_to():
    SPECIFIC_TIME_TO = st.session_state.time_to
    print(SPECIFIC_TIME_TO)




with st.sidebar:
    
    sidebar_image = st.image("image.png")
    sidebar_logo = st.logo("LOGO.png",size="large")

    st.divider()
    st.subheader("To download the latest table of readings simply click the :red[GET LATEST READINGS] button below")
    button_get_latest_readings = st.button("GET LATEST READINGS", type="primary", on_click=backend.extract_all_data)
    
    st.divider()
    #endregion


    #region DOWNLOAD CUSTOM TIME AND DATE FROM THE TABLE
    st.subheader("To download specific table of readings you need to choose the date, time and data:")
    first_column, second_column, third_column = st.columns(3)
    
    with first_column:
        date_input_date_picker_from = st.date_input("From",
                                                format="DD-MM-YYYY",
                                                key="date_from",
                                                value=st.session_state.date_from)
                                                #on_change= append_date_from)



        date_input_date_picker_to = st.date_input("To",
                                            format="DD-MM-YYYY",
                                            key="date_to",
                                            value=None,
                                            on_change= append_date_to)

        
    with second_column:
        time_input_time_picker_from = st.time_input("From:",
                                                key="time_from",
                                                value=None,
                                                on_change= append_time_from)
                                                

        time_input_time_picker_to = st.time_input("To:",
                                                key="time_to",
                                                value=None,
                                                on_change= append_time_to)
    

    button_download = st.button("DOWNLOAD", type="primary")

    st.divider()
    #endregion

    




        




with st.expander("Filters"):
        
        pills_first_column,pills_second_column,pills_third_column,pills_fourth_column,pills_fifth_column,pills_sixth_column,pills_seventh_column,pills_eight_column,pills_ninth_column,pills_tenth_column  = st.columns(10)
        list_of_data_first_column = ["Total_Reactive_Energy"
                        ,"Energy_Total_Active_Power_L1L2L3"
                        ,"Energy_Total_Apparent_Power_L1L2L3"
                        ,"Energy_Total_Reactive_Power_L1L2L3"
                        ,"Energy_Reset_Total_Active_Energy_L1L2L3"
                        ,"Energy_Reset_Total_Reactive_Energy_L1L2L3"
                        ,"Energy_Total_Active_Energy_L1L2L3"
                        ,"Energy_Current_L1"
                        ,"Energy_Current_L2","Energy_Current_L3"
                        ,"TT_Reactor_Seals_Cooling_Oil"
                        ,"TT_Flue_Gas_In"
                        ,"TT_Flue_Gas_In_2"
                        ]
        list_of_data_second_column = ["M_IN_5_1_31_State"
                        ,"M_IN_6_1_01_State"
                        ,"M_IN_6_1_02_State"
                        ,"M_IN_8_1_01_State"
                        ,"M_IN_8_2_03_State"
                        ,"M_IN_8_6_01_State"
                        ,"M_IN_8_6_02_State"
                        ,"Afterburner_State"
                        ,"Afterburner_Power_Feedback"
                        ,"Feeder_State"
                        ,"PID_Pressure_Setpoint"
                        ,"PID_Pressure_Status"]
        list_of_data_third_column = ["TT_Flue_Gas_Out"
                        ,"TT_Syngas_Afterheater_Out"
                        ,"TT_Cyclone_1_Outlet"
                        ,"TT_Syngas_Reactor_Out"
                        ,"TT_Wet_Scrubber_Middle"
                        ,"TT_Flue_Gas_Out_2"
                        ,"TT_Flue_Gas_Out_3"
                        ,"PT_Hydraulic_Pressure"
                        ,"PT_Reactor_Inlet"
                        ,"PT_Wet_Scrubber_Cooling"
                        ,"PT_Syngas_Reactor_Out"
                        ,"PT_Cyclone_1_Outlet"]
        list_of_data_fourth_column = ["VSD_HYD_Freq"
                        ,"VSD_RSC_State"
                        ,"VSD_RSC_Freq"
                        ,"VSD_RSM_State"
                        ,"VSD_RSM_Freq"
                        ,"VSD_SBF_State"
                        ,"VSD_SBF_Freq"
                        ,"VSD_SBM_State"
                        ,"VSD_SBM_Freq"
                        ,"VSD_SBSF_State"
                        ,"VSD_SBSF_Freq"
                        ,"VSD_SAMP_State"
                        ]
        list_of_data_fift_column = ["VSD_SAMP_Freq"
                        ,"M_IN_4_3_09_State"
                        ,"M_IN_4_3_10_State"
                        ,"M_IN_4_9_01_State"
                        ,"M_IN_5_1_02_State"
                        ,"M_IN_5_1_04_State"
                        ,"PID_Wet_Scrubber_Setpoint"
                        ,"PID_Wet_Scrubber_Status"
                        ,"SV_IN_2_2_21_State"
                        ,"SV_IN_3_1_21_State"
                        ,"SV_IN_3_1_22_State"
                        ,"SV_IN_3_3_21_State"]
        list_of_data_sixth_column = ["SV_IN_4_3_60_State"
                        ,"SV_IN_6_1_21_State"
                        ,"SV_IN_4_3_11_State"
                        ,"EMV_IN_5_1_21_State"
                        ,"EMV_IN_5_1_22_State"
                        ,"EMV_IN_5_1_23_State"
                        ,"EMV_IN_5_1_24_State"
                        ,"EMV_IN_5_1_29_State"
                        ,"FFV_IN_6_1_03_State"
                        ,"FFV_IN_6_1_04_State"
                        ,"FFV_IN_6_1_05_State"
                        ,"FFV_IN_6_1_06_State"]
        list_of_data_seventh_column = ["SV_IN_3_5_21_State"
                        ,"SV_IN_3_5_22_State"
                        ,"SV_IN_4_3_21_State"
                        ,"Syngas_Net_Calorific_Value_1"
                        ,"Syngas_Net_Calorific_Value_2"
                        ,"Syngas_Gross_Calorific_Value"
                        ,"Syngas_Temperature"
                        ,"Syngas_Sample_Flow"
                        ,"Syngas_Pressure"
                        ,"Syngas_Mixture_CH4"
                        ,"Syngas_Mixture_CO"
                        ,"Syngas_Mixture_CO2"]
        list_of_data_eighth_column = ["Syngas_N2"
                        ,"Syngas_O2"
                        ,"Syngas_Mixture_H2S"
                        ,"Syngas_Mixture_N2"
                        ,"Syngas_Mixture_O2"
                        ,"Machine_State"
                        ,"VSD_COF_State"
                        ,"VSD_COF_Freq"
                        ,"VSD_CONV_State"
                        ,"VSD_CONV_Freq"
                        ,"VSD_DP2_State"
                        ,"VSD_DP2_Freq"
                        ]
        list_of_data_ninth_column = ["LT_Wet_Scrubber_Inlet"
                        ,"FM_Volume_Flow"
                        ,"FM_Mass_Flow"
                        ,"VSD_HYD_State"
                        ,"Syngas_Mixture_H2"
                        ,"FM_Energy_Flow"
                        ,"FM_Flow_Velocity"
                        ,"FM_Temperature"
                        ,"FM_Calorific_Value"
                        ,"FM_Pressure"
                        ,"Syngas_CH4"
                        ,"Syngas_CO"]
        list_of_data_tenth_column = ["PT_Syngas_Afterheater_Out"
                        ,"PT_Syngas_Storage_Pressure"
                        ,"PT_Flue_Gas_In"
                        ,"PT_Active_Carbon_Outlet"
                        ,"PT_Active_Carbon_Inlet"
                        ,"AT_pH_Meter_Filtering_Tanks"
                        ,"LT_Wet_Scrubber_Outlet"
                        ,"Syngas_CO2"
                        ,"Syngas_H2"
                        ,"Syngas_H2S"]
      

        with pills_first_column:
            st.pills("a",selection_mode="multi",options=list_of_data_first_column,label_visibility="hidden",key="first_group_of_pills")
        with pills_second_column:
            st.pills("b",selection_mode="multi",options=list_of_data_second_column,label_visibility="hidden",key="second_group_of_pills")
        with pills_third_column:
            st.pills("c",selection_mode="multi",options=list_of_data_third_column,label_visibility="hidden",key="third_group_of_pills")
        with pills_fourth_column:
            st.pills("d",selection_mode="multi",options=list_of_data_fourth_column,label_visibility="hidden",key="fourth_group_of_pills")
        with pills_fifth_column:
            st.pills("f",selection_mode="multi",options=list_of_data_fift_column,label_visibility="hidden",key="fifth_group_of_pills")
        with pills_sixth_column:
            st.pills("g",selection_mode="multi",options=list_of_data_sixth_column,label_visibility="hidden",key="sixth_group_of_pills")
        with pills_seventh_column:
            st.pills("h",selection_mode="multi",options=list_of_data_seventh_column,label_visibility="hidden",key="seventh_group_of_pills")
        with pills_eight_column:
            st.pills("j",selection_mode="multi",options=list_of_data_eighth_column,label_visibility="hidden",key="eight_group_of_pills")
        with pills_ninth_column:
            st.pills("k",selection_mode="multi",options=list_of_data_ninth_column,label_visibility="hidden",key="ninth_group_of_pills")
        with pills_tenth_column:
            st.pills("l",selection_mode="multi",options=list_of_data_tenth_column,label_visibility="hidden",key="tenth_group_of_pills")
        
        st.divider()

        button_generate_column, button_reset_filters_column = st.columns([1,9])
        with button_generate_column:
            button_generate = st.button("GENERATE", type="primary", on_click=backend.extract_specific_data_withouth_date_and_time)
        with button_reset_filters_column:
            button_reset_filters = st.button("RESET FILTERS", type="primary",on_click=reset_filters)


if "dataframe" not in st.session_state:
    st.session_state.dataframe = pd.DataFrame()



st.write(st.session_state)