import streamlit as st

on = st.toggle(
    # A short label explaining to the user what this toggle is for.
    label="切换按钮"
)

if on:
    st.write("切换成功")
