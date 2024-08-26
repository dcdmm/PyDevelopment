import streamlit as st

st.page_link(page="pages/matplotlib_f.py",  # 启动脚本文件(app.py)同目录pages目录(目录名必须为pages)下matplotlib_f.py web页面
             # The label for the page link. Labels are required for external pages
             label="pages/matplotlib_f.py链接",
             # If icon is None (default), no icon is displayed.
             icon="1️⃣"
             )
st.page_link(page="pages/plotly_f.py",  # 启动脚本文件(app.py)同目录pages目录(目录名必须为pages)下plotly_f.py web页面
             label="pages/plotly_f.py链接", icon="2️⃣")
st.page_link(page="http://www.baidu.com",  # 外部页面URL链接
             label="百度链接", icon="🌎")
