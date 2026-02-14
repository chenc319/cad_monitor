### ---------------------------------------------------------------------------------------- ###
### -------------------------------- PACKAGES AND FUNCTIONS -------------------------------- ###
### ---------------------------------------------------------------------------------------- ###

### IMPORT OTHER SCRIPTS ###
import streamlit as st
import pandas as pd
import app_boc_activity
import app_cad_repo

### ---------------------------------------------------------------------------------------- ###
### --------------------------------- CONFIGURE STREAMLIT ---------------------------------- ###
### ---------------------------------------------------------------------------------------- ###

### CONFIGURE PAGE SETTINGS ###
st.set_page_config(
    page_title="Mistral CAD Monitor",
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
        margin-right: 10px;
    }

    /* ----- Mistral sidebar theming ----- */

    /* Sidebar background */
    [data-testid="stSidebar"] {
        background-color: #0F3B2E;  /* Mistral green */
    }

    /* Sidebar text color */
    [data-testid="stSidebar"] * {
        color: #FFFFFF !important;
    }

    /* Optional: tweak selectboxes and date inputs in sidebar */
    [data-testid="stSidebar"] .stSelectbox,
    [data-testid="stSidebar"] .stDateInput {
        background-color: #0F3B2E;
    }
    </style>
""", unsafe_allow_html=True)


### SIDEBAR ###
st.sidebar.title("Mistral CAD Monitor")
start_dt = st.sidebar.date_input("Start Date", value=pd.to_datetime('1999-12-31'))
end_dt = st.sidebar.date_input("End Date", value=pd.to_datetime('today'))

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
            "Balance Sheet": "Balance Sheet"
        },
        "Repo": {
            "Select an option...": "Select an option...",
            "CORRA": "CORRA"
        }
    }

    # Initialize session state for each section if not exists
    for section in sections:
        if f"{section}_selection" not in st.session_state:
            st.session_state[f"{section}_selection"] = "Select an option..."

    # Create section headers and selectboxes
    st.markdown("### BoC Activity")
    boc_activity = st.selectbox(
        "BoC Activity",
        list(sections["BoC Activity"].keys()),
        key="BoC Activity_selection",
        on_change=lambda: reset_other_selections("BoC Activity"),
        label_visibility="collapsed"
    )

    st.markdown("### Repo")
    repo = st.selectbox(
        "Repo",
        list(sections["Repo"].keys()),
        key="Repo_selection",
        on_change=lambda: reset_other_selections("Repo"),
        label_visibility="collapsed"
    )

    # Set the current page based on any non-default selection
    page = "Select an option..."
    for selection in [boc_activity,
                      repo
                      ]:
        if selection != "Select an option...":
            page = selection
            break

### ---------------------------------------------------------------------------------------- ###
### ------------------------------- BANK OF CANADA ACTIVITY -------------------------------- ###
### ---------------------------------------------------------------------------------------- ###

if page == 'Balance Sheet':
    st.title('Assets')
    app_boc_activity.plot_boc_assets(start_dt,end_dt)
    st.title('Liabilities')
    app_boc_activity.plot_boc_liabilities(start_dt,end_dt)


### ---------------------------------------------------------------------------------------- ###
### --------------------------------------- CAD REPO --------------------------------------- ###
### ---------------------------------------------------------------------------------------- ###

elif page == 'CORRA':
    st.title("CORRA Rate Complex")
    app_cad_repo.plot_corra_rate_complex(start_dt,end_dt)
    st.title("CORRA Total and Trimmed Volume")
    app_cad_repo.plot_corra_volumes(start_dt,end_dt)

