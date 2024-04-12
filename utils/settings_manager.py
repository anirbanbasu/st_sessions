"""Settings manager module"""

import os
import streamlit as st


def load_settings():
    """Load settings from environment variables or initialise them with default values"""
    if "settings__shell" not in st.session_state:
        st.session_state.settings__shell = os.getenv("SHELL", "/bin/bash")
    if (
        "settings__shell" in st.session_state
        and "shadow__settings__shell" not in st.session_state
    ):
        st.session_state.shadow__settings__shell = st.session_state.settings__shell

    if "settings__user" not in st.session_state:
        st.session_state.settings__user = os.getenv("USER", "!unknown user!")
    if (
        "settings__user" in st.session_state
        and "shadow__settings__user" not in st.session_state
    ):
        st.session_state.shadow__settings__user = st.session_state.settings__user

    if "first_run" not in st.session_state:
        st.session_state.first_run = False


def update_settings():
    """Update settings from the UI"""
    st.session_state.settings__shell = st.session_state.shadow__settings__shell
    st.session_state.settings__user = st.session_state.shadow__settings__user
