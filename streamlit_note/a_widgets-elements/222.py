import streamlit as st

# 设置页面标题
st.title("文件上传器")

# 添加文件上传组件
uploaded_file = st.file_uploader("选择一个文件", type=['txt', 'csv', 'pdf', 'jpg', 'png'])

# 处理上传的文件
if uploaded_file is not None:
    # 显示文件信息
    st.write("### 文件信息")
    st.write(f"文件名: {uploaded_file.name}")
    st.write(f"文件类型: {uploaded_file.type}")
    st.write(f"文件大小: {uploaded_file.size} 字节")
    
    # 根据文件类型进行不同处理
    if uploaded_file.type in ['text/plain', 'text/csv']:
        # 读取文本文件内容
        content = uploaded_file.read().decode('utf-8')
        st.write("### 文件内容预览")
        st.text_area("内容", content, height=200)
    elif uploaded_file.type in ['image/jpeg', 'image/png']:
        # 显示图片
        st.write("### 图片预览")
        st.image(uploaded_file)
    else:
        st.write("### 提示")
        st.write("已上传文件，但当前仅支持文本文件和图片的预览")
else:
    st.write("请上传一个文件")