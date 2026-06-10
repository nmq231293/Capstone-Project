import streamlit as st

if st.session_state.login_state == False:
    st.switch_page('pages/home.py')

text = st.session_state.text

st.header(f'**:red[{text['withdraw_title']}]**', width='stretch',text_alignment='left')
