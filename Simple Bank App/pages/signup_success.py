import streamlit as st

if st.session_state.login_state == True or st.session_state.signup_state == False:
    st.switch_page('pages/re_submit.py')
    
text = st.session_state.text
    
st.header(f'**:red[{text["signup_success_title"].upper()}]**', width='stretch',text_alignment='center')
# st.session_state.current_page = 'pages/signup_success.py'

st.balloons()
col1, col2, col3 = st.columns(3)
with col2:
    st.success(f'{text["signup_success_message"]} {st.session_state.acc_num}')
    if st.button(f'{text["to_login_button"]}', icon='🔑'):
        st.session_state.previous_page.append(st.session_state.current_page)
        st.session_state.signup_state = False
        st.switch_page('pages/login.py')
    if st.button(f'{text["back_to_home_button"]}', icon='🏡'):
        st.session_state.previous_page.append(st.session_state.current_page)
        st.session_state.signup_state = False
        st.switch_page('pages/home.py')