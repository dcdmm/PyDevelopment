import streamlit as st

# Display a chat input widget.
# When st.chat_input is used in the main body of an app, it will be pinned to the bottom of the page.
prompt = st.chat_input(
    # A placeholder text shown when the chat input is empty. Defaults to "Your message".
    placeholder="Say something"
)

st.write(f"User has sent the following prompt: {prompt}")
