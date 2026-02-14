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
    page_title="CAD Monitor",
    layout="wide",
    initial_sidebar_state="expanded"
)

# THEME + HEADER
st.markdown("""
<style>
:root {
    --mistral-green: #003321;
    --mistral-green-light: #0b3b2e;
    --mistral-bg: #f4f7f6;
}

/* Top brand bar */
.brand-bar {
    position: fixed;
    top: 0; left: 0; right: 0;
    height: 64px;
    padding: 0 32px;
    background-color: var(--mistral-green);
    color: #ffffff;
    display: flex;
    align-items: center;
    justify-content: space-between;
    z-index: 1000;
    border-bottom: 1px solid #002616;
    font-family: "Inter", system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
}

.brand-left {
    display: flex;
    align-items: center;
    gap: 12px;
    font-size: 22px;
    letter-spacing: 0.12em;
}

.brand-right {
    font-size: 16px;
    opacity: 0.9;
}

/* Main background */
main {
    background-color: var(--mistral-bg);
}

/* Push main content below bar */
main .block-container {
    padding-top: 88px;
}

/* Sidebar background + text */
section[data-testid="stSidebar"] {
    background-color: var(--mistral-green-light);
    color: #ffffff;
}
section[data-testid="stSidebar"] * {
    color: #ffffff;
}

/* Sidebar form elements as white cards */
section[data-testid="stSidebar"] .stDateInput,
section[data-testid="stSidebar"] .stTextInput,
section[data-testid="stSidebar"] .stSelectbox {
    background-color: #ffffff !important;
    color: #000000 !important;
    border-radius: 6px;
}

/* Sidebar titles */
section[data-testid="stSidebar"] h1,
section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3 {
    color: #ffffff;
}

/* Main titles */
h1, h2, h3 {
    color: var(--mistral-green);
}
</style>

<div class="brand-bar">
  <div class="brand-left">
    <span style="font-size:26px; line-height:1;">≋</span>
    <span>MISTRAL&nbsp;CAPITAL</span>
  </div>
  <div class="brand-right">
    CAD Monitor
  </div>
</div>
""", unsafe_allow_html=True)

### ---------------------------------------------------------------------------------------- ###
### --------------------------------------- SIDEBAR ---------------------------------------- ###
### ---------------------------------------------------------------------------------------- ###

st.sidebar.title("CAD Monitor")
start_dt = st.sidebar.date_input("Start Date", value=pd.to_datetime("1999-12-31"))
end_dt = st.sidebar.date_input("End Date", value=pd.to_datetime("today"))

def reset_other_selections(current_section):
    sections = ["BoC Activity", "Repo"]
    for section in sections:
        if section != current_section:
            st.session_state[f"{section}_selection"] = "Select an option..."

with st.sidebar:
    sections = {
        "BoC Activity": {
            "Select an option...": "Select an option...",
            "Balance Sheet": "Balance Sheet",
        },
        "Repo": {
            "Select an option...": "Select an option...",
            "CORRA": "CORRA",
        },
    }

    for section in sections:
        if f"{section}_selection" not in st.session_state:
            st.session_state[f"{section}_selection"] = "Select an option..."

    st.markdown("### BoC Activity")
    boc_activity = st.selectbox(
        "BoC Activity",
        list(sections["BoC Activity"].keys()),
        key="BoC Activity_selection",
        on_change=lambda: reset_other_selections("BoC Activity"),
        label_visibility="collapsed",
    )

    st.markdown("### Repo")
    repo = st.selectbox(
        "Repo",
        list(sections["Repo"].keys()),
        key="Repo_selection",
        on_change=lambda: reset_other_selections("Repo"),
        label_visibility="collapsed",
    )

    page = "Select an option..."
    for selection in [boc_activity, repo]:
        if selection != "Select an option...":
            page = selection
            break

### ---------------------------------------------------------------------------------------- ###
### ------------------------------- BANK OF CANADA ACTIVITY -------------------------------- ###
### ---------------------------------------------------------------------------------------- ###

if page == "Balance Sheet":
    st.title("Assets")
    app_boc_activity.plot_boc_assets(start_dt, end_dt)
    st.title("Liabilities")
    app_boc_activity.plot_boc_liabilities(start_dt, end_dt)

### ---------------------------------------------------------------------------------------- ###
### --------------------------------------- CAD REPO --------------------------------------- ###
### ---------------------------------------------------------------------------------------- ###

elif page == "CORRA":
    st.title("CORRA")
    st.subheader("CORRA Rate Complex")
    app_cad_repo.plot_corra_rate_complex()
    st.subheader("CORRA Total and Trimmed Volume")
    app_cad_repo.plot_corra_volumes()
