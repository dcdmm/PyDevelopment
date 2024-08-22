import streamlit as st

a = st.slider(
    # A short label explaining to the user what this slider is for.
    label="滑块 a",
    # The minimum permitted value.
    min_value=0,
    # The maximum permitted value.
    max_value=100,
    # The value of the slider when it first renders.
    value=0,
    # The stepping interval.
    step=1
)
st.write("a value: ", a)

b = st.slider("(范围)滑块 b", 0.0, 100.0, [25.0, 75.0], step=0.01)
print(type(b))  # print-><class 'tuple'>
st.write("b value: ", b)
