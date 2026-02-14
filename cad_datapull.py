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
    'CORRA')
with open(Path(DATA_DIR) / 'corra_df.pkl', 'wb') as file:
    pickle.dump(corra_df, file)

corra_compounded_df = get_boc_historical_timeseries(
    'CORRA.COMPOUNDED.INDEX',
    'Compounded CORRA')
with open(Path(DATA_DIR) / 'corra_compounded_df.pkl', 'wb') as file:
    pickle.dump(corra_compounded_df, file)

corra_5_df = get_boc_historical_timeseries(
    'CORRA_RATE_AT_PERCENTILE_5',
    'CORRA 5%')
with open(Path(DATA_DIR) / 'corra_5_df.pkl', 'wb') as file:
    pickle.dump(corra_5_df, file)

corra_25_df = get_boc_historical_timeseries(
    'CORRA_RATE_AT_PERCENTILE_25',
    'CORRA 25%')
with open(Path(DATA_DIR) / 'corra_25_df.pkl', 'wb') as file:
    pickle.dump(corra_25_df, file)

corra_75_df = get_boc_historical_timeseries(
    'CORRA_RATE_AT_PERCENTILE_75',
    'CORRA 75%')
with open(Path(DATA_DIR) / 'corra_75_df.pkl', 'wb') as file:
    pickle.dump(corra_75_df, file)

corra_95_df = get_boc_historical_timeseries(
    'CORRA_RATE_AT_PERCENTILE_95',
    'CORRA 95%')
with open(Path(DATA_DIR) / 'corra_95_df.pkl', 'wb') as file:
    pickle.dump(corra_95_df, file)

### MONEY MARKET YIELDS ###
on_mm_financing_rate_df = get_boc_historical_timeseries(
    'CL.CDN.MOST.1DL',
    'ON MM Rate')
with open(Path(DATA_DIR) / 'on_mm_financing_rate_df.pkl', 'wb') as file:
    pickle.dump(on_mm_financing_rate_df, file)

treasury_bills_1m = get_boc_historical_timeseries(
    'TB.CDN.30D.MID',
    '1m Bills')
with open(Path(DATA_DIR) / 'treasury_bills_1m.pkl', 'wb') as file:
    pickle.dump(treasury_bills_1m, file)

treasury_bills_2m = get_boc_historical_timeseries(
    'TB.CDN.60D.MID',
    '2m Bills')
with open(Path(DATA_DIR) / 'treasury_bills_2m.pkl', 'wb') as file:
    pickle.dump(treasury_bills_2m, file)

treasury_bills_3m = get_boc_historical_timeseries(
    'TB.CDN.90D.MID',
    '3m Bills')
with open(Path(DATA_DIR) / 'treasury_bills_3m.pkl', 'wb') as file:
    pickle.dump(treasury_bills_3m, file)

treasury_bills_6m = get_boc_historical_timeseries(
    'TB.CDN.180D.MID',
    '6m Bills')
with open(Path(DATA_DIR) / 'treasury_bills_6m.pkl', 'wb') as file:
    pickle.dump(treasury_bills_6m, file)

treasury_bills_1y = get_boc_historical_timeseries(
    'TB.CDN.1Y.MID',
    '1y Bills')
with open(Path(DATA_DIR) / 'treasury_bills_1y.pkl', 'wb') as file:
    pickle.dump(treasury_bills_1y, file)


### CORRA TRADING VOLUME ###
corra_total_volume_df = get_boc_historical_timeseries(
    'CORRA_TOTAL_VOLUME',
    'Total Volume')
with open(Path(DATA_DIR) / 'corra_total_volume_df.pkl', 'wb') as file:
    pickle.dump(corra_total_volume_df, file)

corra_trimmed_volume_df = get_boc_historical_timeseries(
    'CORRA_TRIMMED_VOLUME',
    'Trimmed Volume')
with open(Path(DATA_DIR) / 'corra_trimmed_volume_df.pkl', 'wb') as file:
    pickle.dump(corra_trimmed_volume_df, file)

### BOC ASSETS ###
boc_bonds_df = get_boc_historical_timeseries(
    'V36613',
    'GoC Bonds') * 1e6
with open(Path(DATA_DIR) / 'boc_bonds_df.pkl', 'wb') as file:
    pickle.dump(boc_bonds_df, file)

boc_bills_df = get_boc_historical_timeseries(
    'V36612',
    'Treasury Bills') * 1e6
with open(Path(DATA_DIR) / 'boc_bills_df.pkl', 'wb') as file:
    pickle.dump(boc_bills_df, file)

boc_real_return_bonds_df = get_boc_historical_timeseries(
    'V1160788296',
    'Real Return Bonds') * 1e6
with open(Path(DATA_DIR) / 'boc_real_return_bonds_df.pkl', 'wb') as file:
    pickle.dump(boc_real_return_bonds_df, file)

boc_mortgages_df = get_boc_historical_timeseries(
    'V1038114416',
    'Mortgage Bonds') * 1e6
with open(Path(DATA_DIR) / 'boc_mortgages_df.pkl', 'wb') as file:
    pickle.dump(boc_mortgages_df, file)

boc_rrp_df = get_boc_historical_timeseries(
    'V44201362',
    'RRP') * 1e6
with open(Path(DATA_DIR) / 'boc_rrp_df.pkl', 'wb') as file:
    pickle.dump(boc_rrp_df, file)

boc_total_assets_df = get_boc_historical_timeseries(
    'V36610',
    'Total Assets') * 1e6
with open(Path(DATA_DIR) / 'boc_total_assets_df.pkl', 'wb') as file:
    pickle.dump(boc_total_assets_df, file)

### BOC LIABILITIES ###
boc_circulation_notes_df = get_boc_historical_timeseries(
    'V36625',
    'Notes in Circulation') * 1e6
with open(Path(DATA_DIR) / 'boc_circulation_notes_df.pkl', 'wb') as file:
    pickle.dump(boc_circulation_notes_df, file)

boc_goc_dollar_deposits_df = get_boc_historical_timeseries(
    'V36628',
    'GoC Dollar Deposits') * 1e6
with open(Path(DATA_DIR) / 'boc_goc_dollar_deposits_df.pkl', 'wb') as file:
    pickle.dump(boc_goc_dollar_deposits_df, file)

boc_mop_dollar_deposits_df = get_boc_historical_timeseries(
    'V36636',
    'MoP Dollar Deposits') * 1e6
with open(Path(DATA_DIR) / 'boc_mop_dollar_deposits_df.pkl', 'wb') as file:
    pickle.dump(boc_mop_dollar_deposits_df, file)

boc_repo_df = get_boc_historical_timeseries(
    'V1203435186',
    'Repo') * 1e6
with open(Path(DATA_DIR) / 'boc_repo_df.pkl', 'wb') as file:
    pickle.dump(boc_repo_df, file)

boc_total_liabilities_df = get_boc_historical_timeseries(
    'V36624',
    'Total Liabilities') * 1e6
with open(Path(DATA_DIR) / 'boc_total_liabilities_df.pkl', 'wb') as file:
    pickle.dump(boc_total_liabilities_df, file)

### SECURITIES REPO OPERATIONS ###
bank_rate = get_boc_historical_timeseries(
    'V39078',
    'Bank Rate')
with open(Path(DATA_DIR) / 'bank_rate.pkl', 'wb') as file:
    pickle.dump(bank_rate, file)

target_on_rate = get_boc_historical_timeseries(
    'V39079',
    'Target Rate')
with open(Path(DATA_DIR) / 'target_on_rate.pkl', 'wb') as file:
    pickle.dump(target_on_rate, file)

operating_band_low = get_boc_historical_timeseries(
    'V39076',
    'Operating Band Low Rate')
with open(Path(DATA_DIR) / 'operating_band_low.pkl', 'wb') as file:
    pickle.dump(operating_band_low, file)

operating_band_high = get_boc_historical_timeseries(
    'V39077',
    'Operating Band High Rate')
with open(Path(DATA_DIR) / 'operating_band_high.pkl', 'wb') as file:
    pickle.dump(operating_band_high, file)

lynx_settlement_balance_actual = get_boc_historical_timeseries(
    'ACTUAL',
    'Lynx Settlement Balances - Actual')
with open(Path(DATA_DIR) / 'lynx_settlement_balance_actual.pkl', 'wb') as file:
    pickle.dump(lynx_settlement_balance_actual, file)

overnight_repo = get_boc_historical_timeseries(
    'SPRA_OUT',
    'Overnight Repo')
with open(Path(DATA_DIR) / 'overnight_repo.pkl', 'wb') as file:
    pickle.dump(overnight_repo, file)

overnight_rrp = get_boc_historical_timeseries(
    'SRA_OUT',
    'Overnight RRP')
with open(Path(DATA_DIR) / 'overnight_rrp.pkl', 'wb') as file:
    pickle.dump(overnight_rrp, file)

securities_lending = get_boc_historical_timeseries(
    'SEC_LEND',
    'Securities Lending')
with open(Path(DATA_DIR) / 'securities_lending.pkl', 'wb') as file:
    pickle.dump(securities_lending, file)

term_repo = get_boc_historical_timeseries(
    'TERMREPOS',
    'Term Repo')
with open(Path(DATA_DIR) / 'term_repo.pkl', 'wb') as file:
    pickle.dump(term_repo, file)

