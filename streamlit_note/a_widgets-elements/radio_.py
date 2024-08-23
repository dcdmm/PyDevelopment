import streamlit as st

a = st.radio(
    # A short label explaining to the user what this radio group is for.
    label="单选按钮 a",
    # abels for the select options in an Iterable.
    options=["python", "c++", "rust"],
    # A list of captions to show below each radio button. If None (default), no captions are shown.
    captions=[
        "very easy",
        "very fast",
        "very safe",
    ],
)

st.write("a value: ", a)

b = st.radio(
    "单选按钮 b",
    ["china", "japen", "uk"],
    # The index of the preselected option on first render.
    # If None, will initialize empty and return None until the user selects an option. Defaults to 0 (the first option).
    index=None,
)

st.write("b value: ", b)