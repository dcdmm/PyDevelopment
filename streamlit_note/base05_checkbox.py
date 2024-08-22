import streamlit as st

a = st.checkbox(
    # A short label explaining to the user what this checkbox is for.
    label='复选框 a'
)
b = st.checkbox(label='复选框b')
c = st.checkbox(label='复选框c')

if a:
    st.write("a checked", a)

if b:
    st.write("b checked", b)

if c:
    st.write("c checked", c)
