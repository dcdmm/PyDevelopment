import streamlit as st
from openai import OpenAI  # 统一使用openai接口


def clear_chat_history():
    st.session_state.messages = []


def llm_output():
    client = OpenAI(
        api_key=st.session_state.API_key,
        base_url="https://open.bigmodel.cn/api/paas/v4/"  # 智谱AI
    )
    result = client.chat.completions.create(
        model=st.session_state.model,
        messages=[
            {"role": m["role"], "content": m["content"]}
            for m in st.session_state.messages
        ],
        max_tokens=st.session_state.max_tokens,
        temperature=st.session_state.temperature,
        top_p=st.session_state.top_p,
        stream=True  # 流式输出
    )
    return result


with st.sidebar:
    st.title('智谱AI大模型API key对话')
    if 'API_key' in st.session_state and len(st.session_state.API_key) > 1:
        st.success('API key已配置', icon='✅')
    st.text_input('输入API key:', type='password', key='API_key')
    st.selectbox("GLM模型选择", ["GLM-4-0520", "GLM-4-AirX", "GLM-4-Air", "GLM-4-Flash"], key='model')
    st.slider("max_tokens", 0, 2000, value=1024, key='max_tokens')
    st.slider("temperature", 0.0, 1.0, value=0.8, key='temperature')
    st.slider("top_p", 0.0, 1.0, value=0.95, key='top_p')

st.title("💬 Chatbot")
st.caption("🤖 智谱AI聊天机器人")

if "messages" not in st.session_state.keys():
    st.session_state.messages = []

with st.sidebar:
    st.button('清空聊天记录', on_click=clear_chat_history)

# 历史聊天记录展示
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

if prompt := st.chat_input():
    if not st.session_state.API_key:
        st.warning("请先输入您的智谱AI API key")
        st.stop()

    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    with st.chat_message("assistant"):
        response = st.write_stream(llm_output())
    st.session_state.messages.append({"role": "assistant", "content": response})
