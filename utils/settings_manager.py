"""Settings manager module"""

import os
import streamlit as st


def load_settings():
    """Load settings from environment variables or initialise them with default values"""
    if "settings__shell" not in st.session_state:
        st.session_state.settings__shell = os.getenv("SHELL", "/bin/bash")

    if "settings__user" not in st.session_state:
        st.session_state.settings__user = os.getenv("USER", "!unknown user!")

    initialise_shadow_variables()

    if "first_run" not in st.session_state:
        st.session_state.first_run = False


def initialise_shadow_variables():
    """Initialise shadow variables for UI settings"""
    if "settings__shell" in st.session_state:
        st.session_state.shadow__settings__shell = st.session_state.settings__shell
    if "settings__user" in st.session_state:
        st.session_state.shadow__settings__user = st.session_state.settings__user


def update_settings():
    """Update settings from the UI"""
    st.session_state.settings__shell = st.session_state.shadow__settings__shell
    st.session_state.settings__user = st.session_state.shadow__settings__user
