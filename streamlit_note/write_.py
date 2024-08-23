import numpy as np
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# Prints the formatted Markdown string, with support for LaTeX expression, emoji shortcodes, and colored text
st.write("hello world")  # 字符串

md = """## one
```python
import numpy as np

for i in range(10):
    pritn(i)
```

## two
    * 2.1
    * 2.2
    * 2.3
## three
$$ x^2 + y^2 = 1$$"""
st.write(md)

st.write({"a": 1, "b": 2})  # 字典

df = pd.DataFrame(
    {
        "first column": [1, 2, 3, 4],
        "second column": [10, 20, 30, 40],
    }
)
st.write(df)  # pandas DataFrame

y = np.random.normal(0, 1, 1000)
fig, ax = plt.subplots()
ax.hist(y, bins=50)
ax.set_title("normal distribution")
st.write(fig)  # matplotlib figure

data = [[1, 20, 30],
        [20, 1, 60],
        [30, 60, 1]]
fig_px = px.imshow(data,
                   title='Heatmaps in Python')
st.write(fig_px)  # Plotly figure.

# 传递多个参数
st.write("1+1=", "2")
st.write("Below is a DataFrame:", df, "Above is a dataframe.")
