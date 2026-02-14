### ------------------------------------------------------------------------------------ ###
### ------------------------------------- CAD REPO ------------------------------------- ###
### ------------------------------------------------------------------------------------ ###

### PACKAGES ###
from Functions import *
from pathlib import Path
import os
DATA_DIR = os.getenv('DATA_DIR', 'data')

### LOAD DATA ###
with open(Path(DATA_DIR) / 'boc_bonds_df.pkl', 'rb') as file:
    boc_bonds_df = pickle.load(file)
with open(Path(DATA_DIR) / 'boc_bills_df.pkl', 'rb') as file:
    boc_bills_df = pickle.load(file)
with open(Path(DATA_DIR) / 'boc_real_return_bonds_df.pkl', 'rb') as file:
    boc_real_return_bonds = pickle.load(file)
with open(Path(DATA_DIR) / 'boc_mortgages_df.pkl', 'rb') as file:
    boc_mortgages_df = pickle.load(file)
with open(Path(DATA_DIR) / 'boc_rrp_df.pkl', 'rb') as file:
    boc_rrp_df = pickle.load(file)
with open(Path(DATA_DIR) / 'boc_total_assets_df.pkl', 'rb') as file:
    boc_total_assets_df = pickle.load(file)

with open(Path(DATA_DIR) / 'boc_circulation_notes_df.pkl', 'rb') as file:
    boc_circulation_notes_df = pickle.load(file)
with open(Path(DATA_DIR) / 'boc_goc_dollar_deposits_df.pkl', 'rb') as file:
    boc_goc_dollar_deposits_df = pickle.load(file)
with open(Path(DATA_DIR) / 'boc_mop_dollar_deposits_df.pkl', 'rb') as file:
    boc_mop_dollar_deposits_df = pickle.load(file)
with open(Path(DATA_DIR) / 'boc_repo_df.pkl', 'rb') as file:
    boc_repo_df = pickle.load(file)
with open(Path(DATA_DIR) / 'boc_total_liabilities_df.pkl', 'rb') as file:
    boc_total_liabilities_df = pickle.load(file)

### ------------------------------------------------------------------------------------ ###
### ------------------------------------- CAD REPO ------------------------------------- ###
### ------------------------------------------------------------------------------------ ###

boc_assets = merge_dfs([
    boc_bonds_df,
    boc_bills_df,
    boc_real_return_bonds,
    boc_mortgages_df,
    boc_rrp_df,
    boc_total_assets_df
]).dropna()

corra_liabilities = merge_dfs([
    boc_circulation_notes_df,
    boc_goc_dollar_deposits_df,
    boc_mop_dollar_deposits_df,
    boc_repo_df,
    boc_total_liabilities_df,
]).dropna()

def plot_boc_assets():
    streamlit_plot(df=boc_assets,
                   columns_array=boc_assets.columns,
                   colors_array=["#0B2138", "#48DEE9",'#7EC0EE',
                                 '#F9D15B','#F9C846','#F39C12'],
                   graph_title='CORRA Rate Complex',
                   y_axis_label='%')

def plot_boc_liabilities():
    streamlit_plot(df=corra_liabilities,
                   columns_array=corra_liabilities.columns,
                   colors_array=["#0B2138", "#48DEE9",'#7EC0EE','#F9D15B','#F9C846'],
                   graph_title='CORRA Total and Trimmed Volume',
                   y_axis_label='%')