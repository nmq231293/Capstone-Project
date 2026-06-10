import streamlit as st
import time

if st.session_state.login_state == False:
    st.switch_page('pages/home.py')

text = st.session_state.text

st.header(f'**:red[{text["login_success_title"].upper()}]**', width='stretch',text_alignment='center')

st.balloons()

with st.spinner(f'{text["login_success_spinner"]}'):
    time.sleep(3)
    st.switch_page('pages/home.py')