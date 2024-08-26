import numpy as np
import streamlit as st
import matplotlib.pyplot as plt


st.title("matplotlib figure example")

y = np.random.normal(0, 1, 1000)
fig, ax = plt.subplots()
ax.hist(y, bins=50)
ax.set_title("normal distribution")
st.write(fig)
