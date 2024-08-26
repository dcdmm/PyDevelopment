import streamlit as st
from openai import OpenAI

# 智谱AI
client = OpenAI(
    api_key="9cc4190f4f728c2743b4038ba593cafa.1wWwnSFyy5NczGAf",
    base_url="https://open.bigmodel.cn/api/paas/v4/"
)

st.title("chat demo0")

if "messages" not in st.session_state:
    st.session_state.messages = []

# 历史聊天记录展示
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

if prompt := st.chat_input("What is up?"):  # 海象运算符
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    with st.chat_message("assistant"):
        stream = client.chat.completions.create(
            model="glm-4-flash",
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True
        )
        response = st.write_stream(stream)
    st.session_state.messages.append({"role": "assistant", "content": response})
