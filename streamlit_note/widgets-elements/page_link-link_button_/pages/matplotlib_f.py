import numpy as np
import streamlit as st
import matplotlib.pyplot as plt

st.page_link(page="app.py",  # 启动脚本文件(app.py)web页面
             label="Home页面", icon="🏠")

y = np.random.normal(0, 1, 1000)
fig, ax = plt.subplots()
ax.hist(y, bins=50)
ax.set_title("normal distribution")
st.write(fig)
