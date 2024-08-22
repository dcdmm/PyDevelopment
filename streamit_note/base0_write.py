import numpy as np
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.write("hello world")  # 字符串
st.write({"a": 1, "b": 2})  # 字典

string = """## one
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
st.write(string)  # 支持markdown字符串

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
st.write(fig)  # matplotlib图形

# 传递多个参数
st.write("1+1=", "2")
st.write("Below is a DataFrame:", df, "Above is a dataframe.")
