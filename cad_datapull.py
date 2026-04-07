### ------------------------------------------------------------------------------------ ###
### ------------------------------------- DATAPULL ------------------------------------- ###
### ------------------------------------------------------------------------------------ ###

### PACKAGES ###
from Functions import *
from pathlib import Path
import os
import subprocess
DATA_DIR = os.getenv('DATA_DIR', 'data')

# Directory that contains cad_datapull.py; assumed to be repo root
REPO_DIR = Path(__file__).resolve().parent
DATA_DIR = os.getenv('DATA_DIR', REPO_DIR / 'data')

def git_push_update(message="Auto-update BoC data"):
    """
    Stage data/, commit with a message, and push to origin.
    Assumes REPO_DIR is a valid git repo and origin is configured.
    """
    repo_str = str(REPO_DIR)

    # Stage only the data folder to avoid committing unrelated files
    subprocess.run(
        ["git", "-C", repo_str, "add", "data"],
        check=True
    )

    # Commit; allow failure if there's nothing to commit
    commit_proc = subprocess.run(
        ["git", "-C", repo_str, "commit", "-m", message],
        check=False
    )
    if commit_proc.returncode != 0:
        # Probably "nothing to commit"; skip push
        return

    # Push to origin (current branch)
    subprocess.run(
        ["git", "-C", repo_str, "push"],
        check=True
    )

### ------------------------------------------------------------------------------------ ###
### ------------------------------------- DATAPULL ------------------------------------- ###
### ------------------------------------------------------------------------------------ ###

def update_all_data():
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

    ### LYNX ###
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
        'Lynx Settlement Balances - Actual') * 1e6
    with open(Path(DATA_DIR) / 'lynx_settlement_balance_actual.pkl', 'wb') as file:
        pickle.dump(lynx_settlement_balance_actual, file)

    overnight_repo = get_boc_historical_timeseries(
        'SPRA_OUT',
        'Overnight Repo') * 1e6
    with open(Path(DATA_DIR) / 'overnight_repo.pkl', 'wb') as file:
        pickle.dump(overnight_repo, file)

    overnight_rrp = get_boc_historical_timeseries(
        'SRA_OUT',
        'Overnight RRP') * 1e6
    with open(Path(DATA_DIR) / 'overnight_rrp.pkl', 'wb') as file:
        pickle.dump(overnight_rrp, file)

    securities_lending = get_boc_historical_timeseries(
        'SEC_LEND',
        'Securities Lending') * 1e6
    with open(Path(DATA_DIR) / 'securities_lending.pkl', 'wb') as file:
        pickle.dump(securities_lending, file)

    term_repo = get_boc_historical_timeseries(
        'TERMREPOS',
        'Term Repo') * 1e6
    with open(Path(DATA_DIR) / 'term_repo.pkl', 'wb') as file:
        pickle.dump(term_repo, file)

    ### CFTC ###
    with open(Path(DATA_DIR) / 'cftc_all_futures.pkl', 'rb') as file:
        cftc_all_futures = pickle.load(file)

    url = "https://publicreporting.cftc.gov/resource/gpe5-46if.csv?$limit=100"
    response = requests.get(url)
    new_cftc = pd.read_csv(StringIO(response.text))
    new_cftc.columns
    new_cftc.index = pd.to_datetime(new_cftc['report_date_as_yyyy_mm_dd'].values)
    new_cftc.drop('report_date_as_yyyy_mm_dd', axis=1)

    new_cftc['market_and_exchange_names'].unique()

    for each_idx in new_cftc.index:
        if each_idx not in cftc_all_futures.index:
            cftc_all_futures.loc[each_idx] = new_cftc.loc[each_idx]

    with open(Path(DATA_DIR) / 'cftc_all_futures.pkl', 'wb') as file:
        pickle.dump(cftc_all_futures, file)


def cot_year(start_year=2010,
             end_year=2026,
             cot_report_type="traders_in_financial_futures_fut"
             ):
    '''Downloads the selected COT report historical data for a single year
    from the cftc.gov webpage as zip file, unzips the downloaded folder and returns
    the cot data as DataFrame.
    For the current year selection, please note: updates by the CFTC occur typically weekly.
    Once the documents update by CFTC occured, the updated data can be accessed through
    this function. The cot_report_type must match one of the following.

    COT report types:
    "legacy_fut" as report type argument selects the Legacy futures only report,
    "legacy_futopt" the Legacy futures and options report,
    "supplemental_futopt" the Sumpplemental futures and options reports,
    "disaggregated_fut" the Disaggregated futures only report,
    "disaggregated_futopt" the COT Disaggregated futures and options report,
    "traders_in_financial_futures_fut" the Traders in Financial Futures futures only report, and
    "traders_in_financial_futures_fut" the Traders in Financial Futures futures and options report.

    Args:
        cot_report_type (str): selection of the COT report type. Defaults to "legacy_fut" (Legacy futures only report).
        cot_year(int) = year specification as YYYY

    Returns:
        A DataFrame with differing variables (depending on the selected report type).

    Raises:
        ValueError: Raises an exception and returns the argument options.'''
    if cot_report_type == "legacy_fut":
        rep = "deacot"
        txt = "annual.txt"

    elif cot_report_type == "legacy_futopt":
        rep = "deahistfo"
        txt = "annualof.txt"

    elif cot_report_type == "supplemental_futopt":
        rep = "dea_cit_txt_"
        txt = "annualci.txt"

    elif cot_report_type == "disaggregated_fut":
        rep = "fut_disagg_txt_"
        txt = "f_year.txt"

    elif cot_report_type == "disaggregated_futopt":
        rep = "com_disagg_txt_"
        txt = "c_year.txt"

    elif cot_report_type == "traders_in_financial_futures_fut":
        rep = "fut_fin_txt_"
        txt = "FinFutYY.txt"

    elif cot_report_type == "traders_in_financial_futures_futopt":
        rep = "com_fin_txt_"
        txt = "FinComYY.txt"

    else:
        raise ValueError(
            'cot_report_type must be one of: '
            '"legacy_fut", "legacy_futopt", "supplemental_futopt", '
            '"disaggregated_fut", "disaggregated_futopt", '
            '"traders_in_financial_futures_fut", '
            '"traders_in_financial_futures_futopt"'
        )

    dfs = []

    for year in range(start_year, end_year + 1):
        print(f"Downloading year {year} ...")

        url = f"https://cftc.gov/files/dea/history/{rep}{year}.zip"
        r = requests.get(url)
        r.raise_for_status()

        with zipfile.ZipFile(io.BytesIO(r.content)) as zf:
            with zf.open(txt) as f:
                df_year = pd.read_csv(f, low_memory=False)

        df_year["cot_year"] = year
        dfs.append(df_year)

    if not dfs:
        raise RuntimeError("No data downloaded; check year range or report type.")

    return pd.concat(dfs, ignore_index=True)

test_cot = cot_year()

rates_cftc_market_exchange_names = [
    'EURO SHORT TERM RATE - CHICAGO MERCANTILE EXCHANGE',
    '2 YEAR ERIS SOFR SWAP - CHICAGO BOARD OF TRADE',
    '3 YEAR ERIS SOFR SWAP - CHICAGO BOARD OF TRADE',
    '5 YEAR ERIS SOFR SWAP - CHICAGO BOARD OF TRADE',
    '10 YEAR ERIS SOFR SWAP - CHICAGO BOARD OF TRADE',

    'UST BOND - CHICAGO BOARD OF TRADE',
    'ULTRA UST BOND - CHICAGO BOARD OF TRADE',
    'UST 2Y NOTE - CHICAGO BOARD OF TRADE',
    'UST 10Y NOTE - CHICAGO BOARD OF TRADE',
    'ULTRA UST 10Y - CHICAGO BOARD OF TRADE',
    'MICRO 10 YEAR YIELD - CHICAGO BOARD OF TRADE',
    'UST 5Y NOTE - CHICAGO BOARD OF TRADE',
    'FED FUNDS - CHICAGO BOARD OF TRADE',
    'SOFR-3M - CHICAGO MERCANTILE EXCHANGE',
    'SOFR-1M - CHICAGO MERCANTILE EXCHANGE',
]

historical_cot_dict = {}
for contract_name in rates_cftc_market_exchange_names:
    each_df = test_cot[test_cot['Market_and_Exchange_Names'] == contract_name]
    each_df.index = pd.to_datetime(each_df['Report_Date_as_YYYY-MM-DD'])
    each_df.drop([
        'Market_and_Exchange_Names',
        'As_of_Date_In_Form_YYMMDD',
        'Report_Date_as_MM_DD_YYYY',
        'CFTC_Contract_Market_Code',
        'CFTC_Market_Code',
        'CFTC_Region_Code',
        'CFTC_Commodity_Code',
        'CFTC_Contract_Market_Code_Quotes',
        'CFTC_Market_Code_Quotes',
        'CFTC_Commodity_Code_Quotes',
        'CFTC_SubGroup_Code',
        'FutOnly_or_Combined',
        'cot_year',
        'Report_Date_as_YYYY-MM-DD'
    ], axis=1, inplace=True)
    historical_cot_dict[contract_name] = each_df.sort_index()

historical_cot_dict[list(historical_cot_dict.keys())[4]]


