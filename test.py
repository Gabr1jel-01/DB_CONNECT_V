import streamlit as st

text_contents = '''This is some text'''
st.download_button("Download some text", text_contents)

st.write(st.session_state)