### ------------------------------------------------------------------------------------ ###
### --------------------------------------- LYNX --------------------------------------- ###
### ------------------------------------------------------------------------------------ ###

### PACKAGES ###
from Functions import *
from pathlib import Path
import os
DATA_DIR = os.getenv('DATA_DIR', 'data')

### LOAD DATA ###
with open(Path(DATA_DIR) / 'bank_rate.pkl', 'rb') as file:
    bank_rate = pickle.load(file)
with open(Path(DATA_DIR) / 'target_on_rate.pkl', 'rb') as file:
    target_on_rate = pickle.load(file)
with open(Path(DATA_DIR) / 'operating_band_low.pkl', 'rb') as file:
    operating_band_low = pickle.load(file)
with open(Path(DATA_DIR) / 'operating_band_high.pkl', 'rb') as file:
    operating_band_high = pickle.load(file)
with open(Path(DATA_DIR) / 'lynx_settlement_balance_actual.pkl', 'rb') as file:
    lynx_settlement_balance_actual = pickle.load(file)
with open(Path(DATA_DIR) / 'overnight_repo.pkl', 'rb') as file:
    overnight_repo = pickle.load(file)
with open(Path(DATA_DIR) / 'overnight_rrp.pkl', 'rb') as file:
    overnight_rrp = pickle.load(file)
with open(Path(DATA_DIR) / 'securities_lending.pkl', 'rb') as file:
    securities_lending = pickle.load(file)
with open(Path(DATA_DIR) / 'term_repo.pkl', 'rb') as file:
    term_repo = pickle.load(file)

### ------------------------------------------------------------------------------------ ###
### --------------------------------------- LYNX --------------------------------------- ###
### ------------------------------------------------------------------------------------ ###

monetary_policy_implementation = merge_dfs([
    bank_rate,
    target_on_rate,
    operating_band_low,
    operating_band_high
]).dropna()

lynx_settlement_balance = merge_dfs([
    lynx_settlement_balance_actual,
    overnight_repo,
    overnight_rrp,
    securities_lending,
    term_repo
]).dropna()

def plot_monetary_policy_implementation():
    streamlit_plot(df=monetary_policy_implementation,
                   columns_array=monetary_policy_implementation.columns,
                   colors_array=["#0B2138", "#48DEE9", '#7EC0EE', '#F9D15B'],
                   graph_title='Monetary Policy Implementation',
                   y_axis_label='')

def plot_lynx_settlement_balance():
    streamlit_plot(df=lynx_settlement_balance,
                   columns_array=lynx_settlement_balance.columns,
                   colors_array=["#0B2138", "#48DEE9", '#7EC0EE', '#F9D15B', '#F9C846'],
                   graph_title='Lynx Settlement Balance',
                   y_axis_label='')