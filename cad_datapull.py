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

### BOC ASSETS ###
boc_bonds_df = get_boc_historical_timeseries(
    'V36613',
    'boc_bonds')
with open(Path(DATA_DIR) / 'boc_bonds_df.pkl', 'wb') as file:
    pickle.dump(boc_bonds_df, file)

boc_bills_df = get_boc_historical_timeseries(
    'V36612',
    'boc_bills')
with open(Path(DATA_DIR) / 'boc_bills_df.pkl', 'wb') as file:
    pickle.dump(boc_bills_df, file)

boc_real_return_bonds_df = get_boc_historical_timeseries(
    'V1160788296',
    'boc_real_return_bonds')
with open(Path(DATA_DIR) / 'boc_real_return_bonds_df.pkl', 'wb') as file:
    pickle.dump(boc_real_return_bonds_df, file)

boc_mortgages_df = get_boc_historical_timeseries(
    'V1038114416',
    'boc_mortgages')
with open(Path(DATA_DIR) / 'boc_mortgages_df.pkl', 'wb') as file:
    pickle.dump(boc_mortgages_df, file)

boc_rrp_df = get_boc_historical_timeseries(
    'V44201362',
    'boc_rrp')
with open(Path(DATA_DIR) / 'boc_rrp_df.pkl', 'wb') as file:
    pickle.dump(boc_rrp_df, file)

boc_total_assets_df = get_boc_historical_timeseries(
    'V36610',
    'boc_total_assets')
with open(Path(DATA_DIR) / 'boc_total_assets_df.pkl', 'wb') as file:
    pickle.dump(boc_total_assets_df, file)

### BOC LIABILITIES ###
boc_circulation_notes_df = get_boc_historical_timeseries(
    'V36625',
    'boc_notes_in_circulation')
with open(Path(DATA_DIR) / 'boc_circulation_notes_df.pkl', 'wb') as file:
    pickle.dump(boc_circulation_notes_df, file)

boc_goc_dollar_deposits_df = get_boc_historical_timeseries(
    'V36628',
    'boc_goc_dollar_deposits')
with open(Path(DATA_DIR) / 'boc_goc_dollar_deposits_df.pkl', 'wb') as file:
    pickle.dump(boc_goc_dollar_deposits_df, file)

boc_mop_dollar_deposits_df = get_boc_historical_timeseries(
    'V36636',
    'boc_mop_dollar_deposits')
with open(Path(DATA_DIR) / 'boc_mop_dollar_deposits_df.pkl', 'wb') as file:
    pickle.dump(boc_mop_dollar_deposits_df, file)

boc_repo_df = get_boc_historical_timeseries(
    'V1203435186',
    'boc_repo')
with open(Path(DATA_DIR) / 'boc_repo_df.pkl', 'wb') as file:
    pickle.dump(boc_repo_df, file)

boc_total_liabilities_df = get_boc_historical_timeseries(
    'V36624',
    'boc_total_liabilities')
with open(Path(DATA_DIR) / 'boc_total_liabilities_df.pkl', 'wb') as file:
    pickle.dump(boc_total_liabilities_df, file)



