import streamlit as st
import plotly.express as px

st.title("plotly figure example")

data = [[1, 20, 30],
        [20, 1, 60],
        [30, 60, 1]]
fig_px = px.imshow(data,
                   title='Heatmaps in Python')
st.write(fig_px)
