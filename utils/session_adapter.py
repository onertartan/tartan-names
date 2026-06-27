from dataclasses import dataclass

import streamlit as st


class SessionAdapter:
    """
    A clean wrapper for Streamlit session_state.
    Provides namespacing, safer access, and testability.
    """

    def __init__(self, namespace: str):
        self.namespace = namespace

    def _full_key(self, key: str) -> str:
        return f"{key}_{self.namespace}"

    def get(self, key: str, default=None):
        return st.session_state.get(self._full_key(key), default)

    def set(self, key: str, value):
        st.session_state[self._full_key(key)] = value
@dataclass(frozen=True)
class PageKeys:
    """Single source of truth for a page's session_state key names."""
    page_name: str

    @property
    def gender(self):           return f"gender_radio_widget_{self.page_name}"
    @property
    def n_clusters(self):       return f"n_clusters_{self.page_name}"
    @property
    def aggregate_totals(self): return f"aggregate_totals_{self.page_name}"
    @property
    def selected_names(self):   return f"names_{self.page_name}"

    # global (page-independent) keys — plain constants
    SCALER = "scaler"
    GEO_SCALE = "geo_scale"
    YEAR_1, YEAR_2 = "year_1", "year_2"