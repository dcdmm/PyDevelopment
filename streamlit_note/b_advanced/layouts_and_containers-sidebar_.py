import streamlit as st

# Tip:The sidebar is resizable! Drag and drop the right border of the sidebar to resize it!
with st.sidebar:
    sb = st.selectbox(
        "选择框",
        ["python", "c++", "rust"]
    )

with st.sidebar:
    r = st.radio(
        "单选按钮",
        ["china", "usa"]
    )
