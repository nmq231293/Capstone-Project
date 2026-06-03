import streamlit as st
from helpers import login_form, switch_page_confirm

if st.session_state.login_state == True:
    st.switch_page('pages/re_submit.py')
    
st.header('**:red[ĐĂNG NHẬP]**', width='stretch',text_alignment='left')
# st.session_state.current_page = 'pages/login.py'

login_form()
if st.button('Quay về trang chủ', icon='🏡'):
    switch_page_confirm('pages/home.py')