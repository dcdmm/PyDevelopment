import streamlit as st
from openai import OpenAI  # 统一使用openai接口



def clear_chat_history():
    st.session_state.messages = [{"role": "assistant", "content": "你好我是ChatGPT，有什么可以帮助你的？"}]


def ask_gpt(key, model, max_tokens, temperature):
    client = OpenAI(
        api_key=key,
        base_url="https://open.bigmodel.cn/api/paas/v4/"
    )
    result = client.chat.completions.create(
        model="glm-4-flash",
        messages=[
            {"role": m["role"], "content": m["content"]}
            for m in st.session_state.messages
        ],
        stream=True
    )
    return result


with st.sidebar:
    st.title('智谱AI大模型API key对话')
    if 'API_key' in st.session_state and len(st.session_state['API_key']) > 1:
        st.success('API key已经配置', icon='✅')
        key = st.session_state['API_key']
    else:
        key = ""

    key = st.text_input('输入API key:', type='password', value=key)

    st.session_state['API_key'] = key

    model = st.selectbox("GLM模型选择", ["GLM-4-0520", "GLM-4-AirX", "GLM-4-Air", "GLM-4-Flash"])
    max_tokens = st.slider("max_tokens", 0, 2000, value=512)
    temperature = st.slider("temperature", 0.0, 2.0, value=0.8)

if "messages" not in st.session_state.keys():
    st.session_state.messages = []

# 历史聊天记录展示
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

with st.sidebar:
    st.button('清空聊天记录', on_click=clear_chat_history)

if len(key) > 1:
    if prompt := st.chat_input():
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.write(prompt)

        with st.chat_message("assistant"):
            response = st.write_stream(ask_gpt(key, model, max_tokens, temperature))
        st.session_state.messages.append({"role": "assistant", "content": response})
