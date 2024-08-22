import streamlit as st
from pandas.core.interchange.from_dataframe import primitive_column_to_ndarray

# st.title("Hello World")
#
# """
# # My first app
# Here's our first attempt at using data to create a table:
# """
#
# import streamlit as st
# import pandas as pd
# df = pd.DataFrame({
#   'first column': [1, 2, 3, 4],
#   'second column': [10, 20, 30, 40]
# })
#
# df
#
# import streamlit as st
# import pandas as pd
#
# st.write("Here's our first attempt at using data to create a table:")
# st.write(pd.DataFrame({
#     'first column': [1, 2, 3, 4],
#     'second column': [10, 20, 30, 40]
# }))
#
#
# import streamlit as st
# import numpy as np
#
# dataframe = np.random.randn(10, 20)
# st.dataframe(dataframe)
#
#
#
#
# import pandas as pd
# import numpy as np
#
# np.random.seed(24)
# df = pd.DataFrame({'A': np.linspace(1, 10, 10)})
# df = pd.concat([df, pd.DataFrame(np.random.randn(10, 4), columns=list('BCDE'))],
#                axis=1)
# df.iloc[0, 2] = np.nan
#
# def color_negative_red(val):
#     """
#     Takes a scalar and returns a string with
#     the css property `'color: red'` for negative
#     strings, black otherwise.
#     """
#     color = 'red' if val < 0 else 'black'
#     return 'color: %s' % color # 颜色设置
#
# s = df.style.applymap(color_negative_red) # 按元素运行
# st.dataframe(s)
# s
# st.table(s)
#
# import streamlit as st
# import numpy as np
# import pandas as pd
#
# chart_data = pd.DataFrame(
#      np.random.randn(20, 3),
#      columns=['a', 'b', 'c'])
#
# st.line_chart(chart_data)
#
# import streamlit as st
# x = st.slider('x')  # 👈 this is a widget
# st.write(x, 'squared is', x * x)
#
# import streamlit as st
# import numpy as np
# import pandas as pd
#
# if st.checkbox('Show dataframe'):
#     chart_data = pd.DataFrame(
#        np.random.randn(20, 3),
#        columns=['a', 'b', 'c'])
#
#     chart_data
#
# import streamlit as st
# import pandas as pd
#
# df = pd.DataFrame({
#     'first column': [1, 2, 3, 4],
#     'second column': [10, 20, 30, 40]
#     })
#
# option = st.selectbox(
#     'Which number do you like best?',
#      df['first column'])
#
# 'You selected: ', option
#
# import streamlit as st
#
# # Add a selectbox to the sidebar:
# add_selectbox = st.sidebar.selectbox(
#     'How would you like to be contacted?',
#     ('Email', 'Home phone', 'Mobile phone')
# )

# Add a slider to the sidebar:
add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)

import streamlit as st

left_column, right_column = st.columns(2)
# You can use a column just like st.sidebar:
left_column.button('Press me!')

# Or even better, call Streamlit functions inside a "with" block:
with right_column:
    chosen = st.radio(
        'Sorting hat',
        ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
    st.write(f"You are in {chosen} house!")