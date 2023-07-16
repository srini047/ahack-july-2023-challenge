import pandas as pd
import pandas_profiling
import streamlit as st

from streamlit_pandas_profiling import st_profile_report

@st.cache_resource(experimental_allow_widgets=True)
def generate_profile_report():
    df = pd.read_csv("archive/cleaned_data.csv")
    profile = df.profile_report()

    st_profile_report(profile)

generate_profile_report()
