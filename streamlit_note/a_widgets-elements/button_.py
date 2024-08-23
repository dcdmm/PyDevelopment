import streamlit as st

b0 = st.button(
    # A short label explaining to the user what this button is for.
    label="Reset",
    # An optional string that specifies the button type.
    # Can be "primary" for a button with additional emphasis or "secondary" for a normal button.
    # Defaults to "secondary".
    type="primary"
)
st.write(b0)

b1 = st.button(label="Reset", type="secondary")
st.write(b1)
