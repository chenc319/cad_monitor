### ---------------------------------------------------------------------------------------- ###
### -------------------------------- PACKAGES AND FUNCTIONS -------------------------------- ###
### ---------------------------------------------------------------------------------------- ###

### IMPORT OTHER SCRIPTS ###
import streamlit as st
import pandas as pd
import app_boc_activity
import app_cad_repo
import app_lynx
import cad_datapull

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

    /* Sidebar headings and labels */
    [data-testid="stSidebar"] h1,
    [data-testid="stSidebar"] h2,
    [data-testid="stSidebar"] h3,
    [data-testid="stSidebar"] label {
        color: #FFFFFF !important;
    }

    /* Selectbox + other inputs: white box, dark text (placeholder + value) */
    [data-testid="stSidebar"] div[data-baseweb="select"] > div {
        background-color: #FFFFFF !important;
        color: #000000 !important;
    }

    [data-testid="stSidebar"] div[data-baseweb="select"] span {
        color: #000000 !important;
    }

    [data-testid="stSidebar"] .stDateInput input,
    [data-testid="stSidebar"] input,
    [data-testid="stSidebar"] textarea {
        background-color: #FFFFFF !important;
        color: #000000 !important;
    }

    /* Dropdown menu options */
    div[role="listbox"] * {
        color: #000000 !important;
    }
    </style>
""", unsafe_allow_html=True)

### SIDEBAR ###
st.sidebar.title("Mistral CAD Monitor")
start_dt = st.sidebar.date_input("Start Date", value=pd.to_datetime('1999-12-31'))
end_dt = st.sidebar.date_input("End Date", value=pd.to_datetime('today'))

# ---- REFRESH DATA BUTTON (here) ----
if st.sidebar.button("Refresh Data"):
    with st.spinner("Updating BoC data..."):
        cad_datapull.update_all_boc_data()
    st.success("BoC data updated.")
# ------------------------------------

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
            "CORRA": "CORRA",
            "Lynx": "Lynx"
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
    app_boc_activity.plot_boc_assets()
    st.title('Liabilities')
    app_boc_activity.plot_boc_liabilities()


### ---------------------------------------------------------------------------------------- ###
### --------------------------------------- CAD REPO --------------------------------------- ###
### ---------------------------------------------------------------------------------------- ###

elif page == 'CORRA':
    st.title("CORRA Rate Complex")
    app_cad_repo.plot_corra_rate_complex()
    st.title("Money Market Yields")
    app_cad_repo.plot_money_market_yields()
    st.title("CORRA Total and Trimmed Volume")
    app_cad_repo.plot_corra_volumes()

### ---------------------------------------------------------------------------------------- ###
### ------------------------------- SECURITIES REPO OPERATION ------------------------------ ###
### ---------------------------------------------------------------------------------------- ###

elif page == 'Lynx':
    st.title("Monetary Policy Implementation")
    app_lynx.plot_monetary_policy_implementation()
    st.title("Lynx Settlement Balance")
    app_lynx.plot_lynx_settlement_balance()
