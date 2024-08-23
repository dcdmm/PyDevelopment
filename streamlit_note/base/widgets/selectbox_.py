import streamlit as st

a = st.selectbox(
    # A short label explaining to the user what this select widget is for.
    label="选择框 a",
    # Labels for the select options in an Iterable.
    options=["python", "c++", "rust"],
)

st.write("a value: ", a)

b = st.selectbox(
    "选择框 b",
    ["china", "usa", "canda"],
    # The index of the preselected option on first render.
    # If None, will initialize empty and return None until the user selects an option. Defaults to 0 (the first option).
    index=None,
    # A string to display when no options are selected. Defaults to "Choose an option".
    placeholder="Select contact method...",
)

st.write("b value:", b)