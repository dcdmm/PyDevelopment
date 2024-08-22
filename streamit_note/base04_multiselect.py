import streamlit as st

a = st.multiselect(
    label="多选框 a",
    options=["Green", "Yellow", "Red", "Blue"],
    # List of default values. Can also be a single value.
    default=["Yellow", "Red"],
)

print(type(a))  # print-><class 'list'>
st.write("a value: ", a)