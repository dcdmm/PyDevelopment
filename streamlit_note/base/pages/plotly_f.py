import streamlit as st
import plotly.express as px

data = [[1, 20, 30],
        [20, 1, 60],
        [30, 60, 1]]
fig_px = px.imshow(data,
                   title='Heatmaps in Python')
st.write(fig_px)

st.page_link(page="i_page_link.py",  # 启动脚本文件(i_page_link.py)web页面
             label="Home", icon="🏠")
