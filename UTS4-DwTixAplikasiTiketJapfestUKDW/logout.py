import streamlit as st

def logout():
    if st.button("logout", type="primary"):
        st.session_state.logged_in = False
        st.session_state.uname = None
        st.session_state.id = None
        st.session_state.role = None
        st.switch_page("app.py")
