import streamlit as st

# Session State is a way to share variables between reruns, for each user session.
# In addition to the ability to store and persist state, Streamlit also exposes the ability to manipulate state using Callbacks.
st.write(st.session_state)  # {}

st.session_state['a'] = 1
# st.session_state.a = 1  # 与上等价
st.write(st.session_state)  # {"a": 1}
st.session_state.a = 2
st.session_state.b = -1
st.write(st.session_state)  # {"a": 2, "b": -1}

st.write('c' in st.session_state)  # False

# KeyError: 'st.session_state has no key "c".
# st.write(st.session_state['c'])

del st.session_state.b
st.write(st.session_state)  # {"a": 2}


