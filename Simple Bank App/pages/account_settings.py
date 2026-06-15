import streamlit as st

if not st.session_state.login_state and not st.session_state.password_change_need:
    st.switch_page('pages/home.py')

text = st.session_state.text