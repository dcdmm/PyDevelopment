import streamlit as st

a = st.multiselect(
    # A short label explaining to the user what this select widget is for.
    label="多选框 a",
    # Labels for the select options in an Iterable.
    options=["Green", "Yellow", "Red", "Blue"],
    # List of default values. Can also be a single value.
    default=["Yellow", "Red"],
)

print(type(a))  # print-><class 'list'>
st.write("a value: ", a)