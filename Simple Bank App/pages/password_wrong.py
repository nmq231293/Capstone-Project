import streamlit as st
import time

text = st.session_state.text

st.header(f'**:red[{text["password_wrong_header"].upper()}]**', width='stretch',text_alignment='center')

with st.spinner(f'{text["redirecting_message"]}'):
    time.sleep(5)
    st.switch_page('pages/home.py')