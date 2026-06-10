import streamlit as st
from helpers import login_form, switch_page_confirm

if st.session_state.login_state == True:
    st.switch_page('pages/re_submit.py')

text = st.session_state.text

st.header(f'**:red[{text["login_title"].upper()}]**', width='stretch',text_alignment='left')

login_form()
if st.button(f'{text["back_to_home_button"]}', icon='🏡'):
    switch_page_confirm('pages/home.py')