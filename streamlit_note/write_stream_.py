import time
import numpy as np
import pandas as pd
import streamlit as st

text = """
Lorem ipsum dolor sit amet, **consectetur adipiscing** elit, sed do eiusmod tempor
incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis
nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
"""


def stream_data():
    for word in text.split(" "):
        yield word + " "
        time.sleep(0.05)

    yield pd.DataFrame(
        np.random.randn(3, 6),
        columns=["a", "b", "c", "d", "e", "f"],
    )

    yield pd.DataFrame(
        np.random.randn(5, 10),
        columns=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"],
    )

    for word in text.split(" "):
        yield (word + " ").upper()
        time.sleep(0.05)


if st.button("Stream data"):
    # Stream a generator, iterable, or stream-like sequence to the app.
    st.write_stream(stream_data)
