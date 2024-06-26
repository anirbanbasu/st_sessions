"""A simple Hello World app in Streamlit"""

import streamlit as st
from utils.settings_manager import (
    initialise_shadow_variables,
    load_settings,
    update_settings,
)

# Setup page metadata and load settings
if "first_run" not in st.session_state or st.session_state.first_run is True:
    st.set_page_config(
        page_title="Streamlit Session State",
        layout="wide",
        initial_sidebar_state="expanded",
        page_icon="🔍",
    )

    load_settings()
else:
    initialise_shadow_variables()

st.title("Streamlit Session State App!")
st.markdown(
    """
    This app demonstrates a bug in Streamlit session states.
    Or, is this expected behaviour :scream:?

    ## User input and session state modification

    Here's the situation. Below, you'll see two text inputs.
    Both are populated by environment variables that have been loaded only once.
    You can edit both text inputs but the corresponding environment variables
    will not be changed. Instead, the session state variables will be updated.
    """
)

col1, col2 = st.columns(2)
settings__shell = col1.text_input(
    "Current shell",
    key="shadow__settings__shell",
    on_change=update_settings,
    help="""
    This displays the current shell as available from the OS environment.
    Changing it will have no effect on the corresponding environment variable.""",
)

settings__user = col2.text_input(
    "Current user",
    key="shadow__settings__user",
    on_change=update_settings,
    help="""
    This displays the current user as available from the OS environment.
    Changing it will have no effect on the corresponding environment variable.""",
)

st.markdown(
    """
    Modying the above inputs, you can change the session state variables.
    The updated values are displayed below.
            """
)

st.code(
    f"""
        SHELL: {st.session_state.settings__shell}
        USER: {st.session_state.settings__user}
        """,
    line_numbers=True,
)

st.markdown(
    """
    ## Where is the bug?

    :point_left: Change to the other page. You will see that the session state variables
    have been reset to their initial values. Is this the expected behaviour :scream:?

    **Note** that there are two sets of session state variables. One set is shadowing the other.
    The shadow set is connected to the user interface elements as keys. The other set isn't.

    ## The fix

    Okay, no, that's not true! The session state variables seems to be not reset. Why?

    1. **Load settings**: Load settings from environment variables or initialise
    them with default values. Store them in session state variables. Do this only
    once for all pages.

    2. **Initialise shadow session state variables**: Create shadow variables 
    for each session state variable as necessary. Initialise shadow variables 
    everytime the page is loaded.

    For details, check the code of this app on 
    [GitHub](https://github.com/anirbanbasu/st_sessions/).
"""
)
