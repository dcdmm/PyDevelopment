import streamlit as st
import pandas as pd
import numpy as np

st.title("pandas dataframe example")

df = pd.DataFrame(
    np.random.randn(5, 10),
    columns=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"],
)

st.write(df)
