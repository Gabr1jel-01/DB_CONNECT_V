import streamlit as st

# Initialize session state for dates if not already set
if "date_from" not in st.session_state:
    st.session_state.date_from = None

if "date_to" not in st.session_state:
    st.session_state.date_to = None

# Create a form for the date inputs
with st.form(key="date_form"):
    st.write("Select date range:")

    # Define columns inside the form
    col1, col2 = st.columns(2)

    with col1:
        date_input_date_picker_from = st.date_input(
            "From",
            format="DD-MM-YYYY",
            key="date_from",
            value=st.session_state.date_from
        )

    with col2:
        date_input_date_picker_to = st.date_input(
            "To",
            format="DD-MM-YYYY",
            key="date_to",
            value=st.session_state.date_to
        )

    # Submit button for the form
    submitted = st.form_submit_button(label="Apply")

# Process the form submission
if submitted:
    st.session_state.date_from = date_input_date_picker_from
    st.session_state.date_to = date_input_date_picker_to

    # Display the selected dates
    st.write(f"Date range: {st.session_state.date_from} to {st.session_state.date_to}")
