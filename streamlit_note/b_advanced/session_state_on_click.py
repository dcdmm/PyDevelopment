import streamlit as st

a = st.text_input(label="文本输入框", key='a')


def clean_text_input():
    st.session_state.a = ""


b1 = st.button(label="清空文本输入框",
               # An optional callback invoked when this button is clicked.
               on_click=clean_text_input
               )
