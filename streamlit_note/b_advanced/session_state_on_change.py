import streamlit as st


def a_to_b():
    if st.session_state.a == 'china':
        st.session_state.b = '中国是一个文明古国'
    if st.session_state.a == 'usa':
        st.session_state.b = '美国是当前世界唯一超级大国'
    if st.session_state.a == 'japan':
        st.session_state.b = '日本非常缺乏资源'


a = st.selectbox("选择框", ["china", "usa", "japean"], key='a',
                 # 支持该参数的API有:
                 # checkbox
                 # multiselect
                 # radio
                 # selectbox
                 # slider
                 # text_input
                 # text_area
                 # toggle
                 on_change=a_to_b  # An optional callback invoked when this checkbox's value changes.
                 )

b = st.text_input(label="文本输入框", key='b')


def low_to_upper():
    st.session_state.d = st.session_state.c.upper()


def upper_to_lower():
    st.session_state.c = st.session_state.d.lower()


st.text_input(label="文本输入框 c", key='c', on_change=low_to_upper)
st.text_input(label="文本输入框 d", key='d', on_change=upper_to_lower)
