import streamlit as st
import plotly.express as px

prompt = st.chat_input(
    # A placeholder text shown when the chat input is empty. Defaults to "Your message".
    placeholder="Say something"
)
st.write(f"User has sent the following prompt: {prompt}")

with st.chat_message(
        # The name of the message author.
        # Can be "human"/"user" or "ai"/"assistant" to enable preset styling and avatars.
        name="ai"
):
    data = [[1, 20, 30],
            [20, 1, 60],
            [30, 60, 1]]
    fig_px = px.imshow(data,
                       title='Heatmaps in Python')
    st.write(fig_px)
