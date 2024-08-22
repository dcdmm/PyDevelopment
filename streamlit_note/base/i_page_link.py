import streamlit as st

st.page_link("pages/matplotlib_f.py",  # 启动脚本文件(i_page_link.py)同目录pages目录(目录名必须为pages)下matplotlib_f.py web页面
             # The label for the page link. Labels are required for external pages
             label="matplotlib figure",
             # If icon is None (default), no icon is displayed.
             icon="1️⃣"
             )
st.page_link("pages/plotly_f.py",  # 启动脚本文件(i_page_link.py)同目录pages目录(目录名必须为pages)下plotly_f.py web页面
             label="plotly figure", icon="2️⃣")
st.page_link("http://www.baidu.com",  # 外部URL
             label="Baidu", icon="🌎")
