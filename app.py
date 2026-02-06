### ---------------------------------------------------------------------------------------- ###
### -------------------------------- PACKAGES AND FUNCTIONS -------------------------------- ###
### ---------------------------------------------------------------------------------------- ###

### IMPORT OTHER SCRIPTS ###
import streamlit as st
import pandas as pd
import functools as ft
import app_boc_activity
import app_cad_repo


### FUNCTIONS ###
def merge_dfs(array_of_dfs):
    new_df = ft.reduce(lambda left,
                              right: pd.merge(left,
                                                    right,
                                                    left_index=True,
                                                    right_index=True,
                                                    how='outer'), array_of_dfs)
    return(new_df)

### ---------------------------------------------------------------------------------------- ###
### --------------------------------- CONFIGURE STREAMLIT ---------------------------------- ###
### ---------------------------------------------------------------------------------------- ###

### CONFIGURE PAGE SETTINGS ###
st.set_page_config(
    page_title="CAD Monitor",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
    <style>
    .header-container {
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        padding: 8px;
        background-color: white;
        z-index: 999;
        border-bottom: 1px solid #f0f2f6;
        font-size: 14px;
    }
    .main {
        margin-top: 60px;
    }
    .stMetric {
        background-color: #ffffff;
        padding: 4px 8px;
        border-radius: 4px;
        display: inline-block;
        margin-right: 10px;a
    }
    </style>
""", unsafe_allow_html=True)

### SIDEBAR ###
st.sidebar.title("CAD Monitor")
start_date = st.sidebar.date_input("Start Date", value=pd.to_datetime('1999-12-31'))
end_date = st.sidebar.date_input("End Date", value=pd.to_datetime('today'))

def reset_other_selections(current_section):
    sections = ["BoC Activity",
                "Repo"
                ]
    for section in sections:
        if section != current_section:
            st.session_state[f"{section}_selection"] = "Select an option..."

with st.sidebar:
    # Create a dictionary mapping sections to their options
    sections = {
        "BoC Activity": {
            "Select an option...": "Select an option...",
            "Summary": "Summary"
        },
        "Repo": {
            "Select an option...": "Select an option...",
            "Summary": "Summary"
        }
    }

    # Initialize session state for each section if not exists
    for section in sections:
        if f"{section}_selection" not in st.session_state:
            st.session_state[f"{section}_selection"] = "Select an option..."

    # Create section headers and selectboxes
    st.markdown("### BoC Activity")
    macro_regime_models = st.selectbox(
        "BoC Activity",
        list(sections["BoC Activity"].keys()),
        key="BoC Activity_selection",
        on_change=lambda: reset_other_selections("BoC Activity"),
        label_visibility="collapsed"
    )

    st.markdown("### Repo")
    demark = st.selectbox(
        "Repo",
        list(sections["Repo"].keys()),
        key="Repo_selection",
        on_change=lambda: reset_other_selections("Repo"),
        label_visibility="collapsed"
    )

    # Set the current page based on any non-default selection
    page = "Select an option..."
    for selection in [macro_regime_models,
                      demark
                      ]:
        if selection != "Select an option...":
            page = selection
            break

### ---------------------------------------------------------------------------------------- ###
### ------------------------------- BANK OF CANADA ACTIVITY -------------------------------- ###
### ---------------------------------------------------------------------------------------- ###

if page == 'Summary':
    st.title('Historical Performance')
    app_sam_coreequity.core_equity_mags_spx()
    st.title('Rolling Alpha')
    app_sam_coreequity.sam_core_equity_rolling_alpha()
    st.title('SAM Core Equity + MAGS Portfolios')
    app_sam_coreequity.core_equity_mag_backtest_simulation()
    st.title('Daily SAM CE vs. SPX')
    app_sam_coreequity.mock_daily_sam_ce_portfolio()

### ---------------------------------------------------------------------------------------- ###
### --------------------------------------- CAD REPO --------------------------------------- ###
### ---------------------------------------------------------------------------------------- ###

elif page == 'Growth & Inflation Study':
    app_growth_inflation.plot_growth_inflation()
    app_growth_inflation.plot_spx_sectors_and_factors_regimes()

