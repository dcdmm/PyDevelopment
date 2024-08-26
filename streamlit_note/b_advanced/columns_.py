import streamlit as st
import numpy as np
import pandas as pd

col1, col2, col3 = st.columns(
    # Controls the number and width of columns to insert. Can be one of:
    # * An integer that specifies the number of columns. All columns have equal width in this case.
    # * An Iterable of numbers (int or float) that specify the relative width of each column. E.g. [0.7, 0.3] creates two columns where the first one takes up 70% of the available with and the second one takes up 30%. Or [1, 2, 3] creates three columns where the second one is two times the width of the first one, and the third one is three times that width.
    spec=[2, 2.5, 1.5],
    # The vertical alignment of the content inside the columns. The default is "top".
    vertical_alignment='top'  # "top" or "center" or "bottom"
)

with col1:
    st.header("A cat")
    st.image("https://static.streamlit.io/examples/cat.jpg")

with col2:
    st.header("A DataFrame")
    st.write(pd.DataFrame(
        np.random.randn(5, 10),
        columns=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"],
    ))

with col3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg")
