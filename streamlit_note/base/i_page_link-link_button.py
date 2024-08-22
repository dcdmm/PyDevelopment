import streamlit as st

st.page_link("pages/matplotlib_f.py",  # 启动脚本文件(i_page_link-link_button.py)同目录pages目录(目录名必须为pages)下matplotlib_f.py web页面
             # The label for the page link. Labels are required for external pages
             label="pages/matplotlib_f.py链接",
             # If icon is None (default), no icon is displayed.
             icon="1️⃣"
             )
st.page_link("pages/plotly_f.py",  # 启动脚本文件(i_page_link-link_button.py)同目录pages目录(目录名必须为pages)下plotly_f.py web页面
             label="pages/plotly_f.py链接", icon="2️⃣")
st.page_link("http://www.baidu.com",  # URL链接
             label="百度链接", icon="🌎")

st.link_button(label="URL链接按钮", url="https://www.bilibili.com/")
