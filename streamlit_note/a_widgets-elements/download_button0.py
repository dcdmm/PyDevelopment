import streamlit as st
import pandas as pd
import numpy as np


df = pd.DataFrame(
    np.random.randn(50, 20), columns=("col %d" % i for i in range(20))
)
csv = df.to_csv().encode("utf-8")

st.write(f"CSV content length: {len(csv)}")
         
st.download_button(
    label="Download CSV",
    # The contents of the file to be downloaded
    data=csv,  # (str, bytes, or file)
    file_name="data.csv",
    # The MIME type of the data.
    # For more information about MIME types, see https://www.iana.org/assignments/media-types/media-types.xhtml.
    mime="text/csv"
)

# 下载文件
with open("image_e0.png", "rb") as file:
    st.download_button(
        label="Download image",
        data=file,
        file_name="cute.png",
        mime="image/png",
    )