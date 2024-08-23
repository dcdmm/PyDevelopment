import streamlit as st

b0 = st.button(
    # A short label explaining to the user what this button is for.
    label="button0",
    # An optional string that specifies the button type.
    # Can be "primary" for a button with additional emphasis or "secondary" for a normal button.
    # Defaults to "secondary".
    type="primary"
)
st.write(b0)

b1 = st.button(label="button1", type="secondary")
st.write(b1)

b2 = st.button(label="button2", type="primary")
st.write(b2)

# 下一次重新加载时,所有值会自动重置为False