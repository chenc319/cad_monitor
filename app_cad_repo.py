### ------------------------------------------------------------------------------------ ###
### ------------------------------------- CAD REPO ------------------------------------- ###
### ------------------------------------------------------------------------------------ ###

### PACKAGES ###
from Functions import *
from pathlib import Path
import os
DATA_DIR = os.getenv('DATA_DIR', 'data')

### LOAD DATA ###
with open(Path(DATA_DIR) / 'corra_df.pkl', 'rb') as file:
    corra_df = pickle.load(file)
with open(Path(DATA_DIR) / 'corra_compounded_df.pkl', 'rb') as file:
    corra_compounded_df = pickle.load(file)
with open(Path(DATA_DIR) / 'corra_5_df.pkl', 'rb') as file:
    corra_5_df = pickle.load(file)
with open(Path(DATA_DIR) / 'corra_25_df.pkl', 'rb') as file:
    corra_25_df = pickle.load(file)
with open(Path(DATA_DIR) / 'corra_75_df.pkl', 'rb') as file:
    corra_75_df = pickle.load(file)
with open(Path(DATA_DIR) / 'corra_95_df.pkl', 'rb') as file:
    corra_95_df = pickle.load(file)
with open(Path(DATA_DIR) / 'corra_total_volume_df.pkl', 'rb') as file:
    corra_total_volume_df = pickle.load(file)
with open(Path(DATA_DIR) / 'corra_trimmed_volume_df.pkl', 'rb') as file:
    corra_trimmed_volume_df = pickle.load(file)

### ------------------------------------------------------------------------------------ ###
### ------------------------------------- CAD REPO ------------------------------------- ###
### ------------------------------------------------------------------------------------ ###

corra_rate_complex = merge_dfs([corra_df,
                                corra_5_df,
                                corra_25_df,
                                corra_75_df,
                                corra_95_df]).dropna()
corra_volume_df = merge_dfs([corra_total_volume_df,
                             corra_trimmed_volume_df]).dropna()

def plot_corra_rate_complex():
    streamlit_plot(df=corra_rate_complex,
                   columns_array=corra_rate_complex.columns,
                   colors_array=["#0B2138", "#48DEE9",'#7EC0EE','#F9D15B','#F9C846'],
                   graph_title='CORRA Rate Complex',
                   y_axis_label='%')

def plot_corra_volumes():
    streamlit_plot(df=corra_volume_df,
                   columns_array=corra_volume_df.columns,
                   colors_array=["#0B2138", "#48DEE9"],
                   graph_title='CORRA Total and Trimmed Volume',
                   y_axis_label='%')

