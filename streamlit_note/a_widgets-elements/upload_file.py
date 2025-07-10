import streamlit as st
import pandas as pd

st.title("文件上传器")

# 一次接受一个文件的文件上传器
uploaded_file = st.file_uploader("选择一个文件", type=['txt', 'csv', 'pdf', 'jpg', 'png'])

if uploaded_file is not None:
    st.write("### 文件信息")
    st.write(f"文件名: {uploaded_file.name}")
    st.write(f"文件类型: {uploaded_file.type}")
    st.write(f"文件大小: {uploaded_file.size} 字节")

    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()

    if uploaded_file.type in ['text/plain']:
        # To read file as string:
        content = uploaded_file.read()
        content = content.decode('utf-8')
        st.write("### 文件内容预览")
        st.text_area("内容", content, height=200)
    elif uploaded_file.type in ['text/csv']:
        dataframe = pd.read_csv(uploaded_file)
        st.write(dataframe)
    elif uploaded_file.type in ['image/jpeg', 'image/png']:
        st.write("### 图片预览")
        st.image(uploaded_file)


# 一次接受多个文件的文件上传器
uploaded_file_multi = st.file_uploader("选择一个文件", type=['txt', 'csv', 'pdf', 'jpg', 'png'], accept_multiple_files=True)
for uploaded_file in uploaded_file_multi:
    st.write(f"文件名: {uploaded_file.name}")