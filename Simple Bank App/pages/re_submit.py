import streamlit as st
import time 

text = st.session_state.text

st.header(f'**:red[{text["re_submit_title"]}]**', width='stretch',text_alignment='center')

with st.spinner(f'{text["redirecting_message"]}'):
    time.sleep(3)
    st.switch_page('pages/home.py')