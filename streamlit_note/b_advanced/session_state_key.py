import streamlit as st

# 支持该参数的API有:
# button
# checkbox
# chat_input
# multiselect
# radio
# selectbox
# slider
# text_input
# text_area
# toggle
b0 = st.button(label="button0: ", type="primary", key='button0')
b1 = st.button(label="button1: ", type="secondary", key='button1')
ci = st.chat_input("chat_input: ", key="chat_input")
cb = st.checkbox(label='checkbox: ', key="checkbox")
ms = st.multiselect("multiselect", ['a', 'b', 'c'], key="multiselect")
r = st.radio("radio: ", ["china", "japen", "uk"], key="radio")
sb = st.selectbox(label="selectbox: ", options=["python", "c++", "rust"], key="selectbox")
s = st.slider("slider: ", 0.0, 100.0, [25.0, 75.0], key="slider")
ti = st.text_input(label="text_input: ", key="text_input")
ta = st.text_area(label="text_area: ", key="text_area")
t = st.toggle(label="toggle: ", key="toggle")

st.write(st.session_state)
