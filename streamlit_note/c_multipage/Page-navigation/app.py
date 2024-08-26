import streamlit as st

pages = {
    "dataframe": [
        st.Page("d0.py",
                # The title of the page.
                title="dataframe 0",
                # An optional emoji or icon to display next to the page title and label.
                # If icon is None (default), no icon is displayed next to the page label in the navigation menu, and a Streamlit icon is displayed next to the title (in the browser tab).
                icon="🔥"
                ),
        st.Page("d1.py", title="dataframe 1", icon='😘'),
    ],
    "figure": [
        st.Page("f0.py", title="figure 0", icon='😂'),
        st.Page("f1.py", title="figure 1"),
    ],
}

# Configure the available pages in a multipage app.
pg = st.navigation(
    # The available pages for the app.
    # To create labeled sections or page groupings within the navigation menu, pages must be a dictionary. Each key is the label of a section and each value is the list of StreamlitPage objects for that section.
    # To create a navigation menu with no sections or page groupings, pages must be a list of StreamlitPage objects.
    pages=pages
)
pg.run()
