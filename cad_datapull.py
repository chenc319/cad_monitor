### ------------------------------------------------------------------------------------ ###
### ------------------------------------- DATAPULL ------------------------------------- ###
### ------------------------------------------------------------------------------------ ###

### PACKAGES ###
from Functions import *
from pathlib import Path
import os
DATA_DIR = os.getenv('DATA_DIR', 'data')

### ------------------------------------------------------------------------------------ ###
### ------------------------------------- DATAPULL ------------------------------------- ###
### ------------------------------------------------------------------------------------ ###

### CORRA RATE ###
corra_df = get_boc_historical_timeseries(
    'AVG.INTWO',
    'corra')
with open(Path(DATA_DIR) / 'corra_df.pkl', 'wb') as file:
    pickle.dump(corra_df, file)

corra_compounded_df = get_boc_historical_timeseries(
    'CORRA.COMPOUNDED.INDEX',
    'compounded_corra')
with open(Path(DATA_DIR) / 'corra_compounded_df.pkl', 'wb') as file:
    pickle.dump(corra_compounded_df, file)

corra_5_df = get_boc_historical_timeseries(
    'CORRA_RATE_AT_PERCENTILE_5',
    'corra_5')
with open(Path(DATA_DIR) / 'corra_5_df.pkl', 'wb') as file:
    pickle.dump(corra_5_df, file)

corra_25_df = get_boc_historical_timeseries(
    'CORRA_RATE_AT_PERCENTILE_25',
    'corra_25')
with open(Path(DATA_DIR) / 'corra_25_df.pkl', 'wb') as file:
    pickle.dump(corra_25_df, file)

corra_75_df = get_boc_historical_timeseries(
    'CORRA_RATE_AT_PERCENTILE_75',
    'corra_75')
with open(Path(DATA_DIR) / 'corra_75_df.pkl', 'wb') as file:
    pickle.dump(corra_75_df, file)

corra_95_df = get_boc_historical_timeseries(
    'CORRA_RATE_AT_PERCENTILE_95',
    'corra_95')
with open(Path(DATA_DIR) / 'corra_95_df.pkl', 'wb') as file:
    pickle.dump(corra_95_df, file)

### CORRA TRADING VOLUME ###
corra_total_volume_df = get_boc_historical_timeseries(
    'CORRA_TOTAL_VOLUME',
    'corra_total_volume')
with open(Path(DATA_DIR) / 'corra_total_volume_df.pkl', 'wb') as file:
    pickle.dump(corra_total_volume_df, file)

corra_trimmed_volume_df = get_boc_historical_timeseries(
    'CORRA_TRIMMED_VOLUME',
    'corra_trimmed_volume')
with open(Path(DATA_DIR) / 'corra_trimmed_volume_df.pkl', 'wb') as file:
    pickle.dump(corra_trimmed_volume_df, file)