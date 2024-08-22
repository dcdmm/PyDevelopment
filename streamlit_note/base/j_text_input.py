import streamlit as st

a = st.text_input(
    # A short label explaining to the user what this input is for.
    label="文本输入框",
    # The text value of this widget when it first renders.
    # This will be cast to str internally.
    # If None, will initialize empty and return None until the user provides input.
    # Defaults to empty string.
    value=None
)
st.write("输入内容为: ", a)
