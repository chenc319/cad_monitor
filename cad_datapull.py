### ------------------------------------------------------------------------------------ ###
### ------------------------------------- DATAPULL ------------------------------------- ###
### ------------------------------------------------------------------------------------ ###

### PACKAGES ###
from Functions import *
from pathlib import Path
import os
DATA_DIR = os.getenv('DATA_DIR', 'data')

### CORRA RATE ###
corra_df = get_boc_historical_timeseries(
    'AVG.INTWO',
    '1990-01-01','corra')
corra_compounded_df = get_boc_historical_timeseries(
    'CORRA.COMPOUNDED.INDEX',
    '1990-01-01','corra')
corra_5_df = get_boc_historical_timeseries(
    'CORRA_RATE_AT_PERCENTILE_5',
    '1990-01-01','corra')
corra_25_df = get_boc_historical_timeseries(
    'CORRA_RATE_AT_PERCENTILE_25',
    '1990-01-01','corra')
corra_75_df = get_boc_historical_timeseries(
    'CORRA_RATE_AT_PERCENTILE_75',
    '1990-01-01','corra')
corra_95_df = get_boc_historical_timeseries(
    'CORRA_RATE_AT_PERCENTILE_95',
    '1990-01-01','corra')

### CORRA TRADING VOLUME ###
corra_total_volume_df = get_boc_historical_timeseries(
    'CORRA_TOTAL_VOLUME',
    '1990-01-01','corra')
corra_trimmed_volume_df = get_boc_historical_timeseries(
    'CORRA_TRIMMED_VOLUME',
    '1990-01-01','corra')