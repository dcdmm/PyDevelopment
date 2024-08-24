import streamlit as st


def a_to_b():
    if st.session_state.a == 'china':
        st.session_state.b = '中国是一个文明古国'
    if st.session_state.a == 'usa':
        st.session_state.b = '美国是当前世界唯一超级大国'
    if st.session_state.a == 'japan':
        st.session_state.b = '日本非常缺乏资源'


a = st.selectbox("选择框", ["china", "usa", "japean"], key='a', on_change=a_to_b)

b = st.text_input(label="文本输入框", key='b')


def c_to_d():
    st.session_state.d = st.session_state.c.upper()


def d_to_c():
    st.session_state.c = st.session_state.d.lower()


st.text_input(label="ti c", key='c', on_change=c_to_d)
st.text_input(label="ti d", key='d', on_change=d_to_c)
