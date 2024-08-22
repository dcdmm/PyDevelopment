import streamlit as st

st.title("title")

st.header("header 1")
st.subheader('subhead 1.1')
# Shows a colored divider below the header.
# If True, successive headers will cycle through divider colors.
# That is, the first header will have a blue line, the second header will have a green line, and so on. If a string, the color can be set to one of the following: blue, green, orange, red, violet, gray/grey, or rainbow.
st.header("header 2", divider=True)
st.subheader('subhead 2.1', divider=True)
st.header("header 3", divider=True)
st.subheader('subhead 3.1', divider=True)
st.header("header 4", divider=True)
st.subheader('subhead 4.1', divider=True)
st.header("header 5", divider='red')
st.subheader('subhead 5.1', divider='red')
st.header("header 6", divider='orange')
st.subheader('subhead 6.1', divider='orange')
