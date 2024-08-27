import streamlit as st

name = st.text_input("Name")

if not name:
    st.warning('Please input a name.')
    # Stops execution immediately.
    # Streamlit will not run any statements after st.stop(). We recommend rendering a message to explain why the script has stopped.
    st.stop()

passwd = st.text_input("Password", type='password')