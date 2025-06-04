import streamlit as st

# Display a success message.
st.success(
    # The info text to display.
    body='This is a success message!',
    # An optional emoji or icon to display next to the alert.
    # If icon is None (default), no icon is displayed.
    icon="✅"
)

# Display an informational message.
st.info('This is a purely informational message', icon="ℹ️")

# Display warning message.
st.warning('This is a warning', icon="⚠️")