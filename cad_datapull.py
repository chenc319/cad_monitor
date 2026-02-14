# update_boc_data.py
from pathlib import Path
import os
import pickle
import requests  # for the SLP JSON call
from Functions import get_boc_historical_timeseries  # your helper

DATA_DIR = Path(os.getenv("DATA_DIR", "data"))
DATA_DIR.mkdir(parents=True, exist_ok=True)

def update_all_boc_data():
    # --- CORRA ---
    corra_df = get_boc_historical_timeseries("AVG.INTWO", "CORRA")
    (DATA_DIR / "corra_df.pkl").write_bytes(pickle.dumps(corra_df))

    corra_compounded_df = get_boc_historical_timeseries("CORRA.COMPOUNDED.INDEX", "Compounded CORRA")
    (DATA_DIR / "corra_compounded_df.pkl").write_bytes(pickle.dumps(corra_compounded_df))

    corra_5_df = get_boc_historical_timeseries("CORRA_RATE_AT_PERCENTILE_5", "CORRA 5%")
    (DATA_DIR / "corra_5_df.pkl").write_bytes(pickle.dumps(corra_5_df))

    corra_25_df = get_boc_historical_timeseries("CORRA_RATE_AT_PERCENTILE_25", "CORRA 25%")
    (DATA_DIR / "corra_25_df.pkl").write_bytes(pickle.dumps(corra_25_df))

    corra_75_df = get_boc_historical_timeseries("CORRA_RATE_AT_PERCENTILE_75", "CORRA 75%")
    (DATA_DIR / "corra_75_df.pkl").write_bytes(pickle.dumps(corra_75_df))

    corra_95_df = get_boc_historical_timeseries("CORRA_RATE_AT_PERCENTILE_95", "CORRA 95%")
    (DATA_DIR / "corra_95_df.pkl").write_bytes(pickle.dumps(corra_95_df))

    # --- Money market yields ---
    on_mm_financing_rate_df = get_boc_historical_timeseries("CL.CDN.MOST.1DL", "ON MM Rate")
    (DATA_DIR / "on_mm_financing_rate_df.pkl").write_bytes(pickle.dumps(on_mm_financing_rate_df))

    treasury_bills_1m = get_boc_historical_timeseries("TB.CDN.30D.MID", "1m Bills")
    (DATA_DIR / "treasury_bills_1m.pkl").write_bytes(pickle.dumps(treasury_bills_1m))

    treasury_bills_2m = get_boc_historical_timeseries("TB.CDN.60D.MID", "2m Bills")
    (DATA_DIR / "treasury_bills_2m.pkl").write_bytes(pickle.dumps(treasury_bills_2m))

    treasury_bills_3m = get_boc_historical_timeseries("TB.CDN.90D.MID", "3m Bills")
    (DATA_DIR / "treasury_bills_3m.pkl").write_bytes(pickle.dumps(treasury_bills_3m))

    treasury_bills_6m = get_boc_historical_timeseries("TB.CDN.180D.MID", "6m Bills")
    (DATA_DIR / "treasury_bills_6m.pkl").write_bytes(pickle.dumps(treasury_bills_6m))

    treasury_bills_1y = get_boc_historical_timeseries("TB.CDN.1Y.MID", "1y Bills")
    (DATA_DIR / "treasury_bills_1y.pkl").write_bytes(pickle.dumps(treasury_bills_1y))

    # --- CORRA trading volume ---
    corra_total_volume_df = get_boc_historical_timeseries("CORRA_TOTAL_VOLUME", "Total Volume")
    (DATA_DIR / "corra_total_volume_df.pkl").write_bytes(pickle.dumps(corra_total_volume_df))

    corra_trimmed_volume_df = get_boc_historical_timeseries("CORRA_TRIMMED_VOLUME", "Trimmed Volume")
    (DATA_DIR / "corra_trimmed_volume_df.pkl").write_bytes(pickle.dumps(corra_trimmed_volume_df))

    # --- BoC assets ---
    boc_bonds_df = get_boc_historical_timeseries("V36613", "GoC Bonds") * 1e6
    (DATA_DIR / "boc_bonds_df.pkl").write_bytes(pickle.dumps(boc_bonds_df))

    boc_bills_df = get_boc_historical_timeseries("V36612", "Treasury Bills") * 1e6
    (DATA_DIR / "boc_bills_df.pkl").write_bytes(pickle.dumps(boc_bills_df))

    boc_real_return_bonds_df = get_boc_historical_timeseries("V1160788296", "Real Return Bonds") * 1e6
    (DATA_DIR / "boc_real_return_bonds_df.pkl").write_bytes(pickle.dumps(boc_real_return_bonds_df))

    boc_mortgages_df = get_boc_historical_timeseries("V1038114416", "Mortgage Bonds") * 1e6
    (DATA_DIR / "boc_mortgages_df.pkl").write_bytes(pickle.dumps(boc_mortgages_df))

    boc_rrp_df = get_boc_historical_timeseries("V44201362", "RRP") * 1e6
    (DATA_DIR / "boc_rrp_df.pkl").write_bytes(pickle.dumps(boc_rrp_df))

    boc_total_assets_df = get_boc_historical_timeseries("V36610", "Total Assets") * 1e6
    (DATA_DIR / "boc_total_assets_df.pkl").write_bytes(pickle.dumps(boc_total_assets_df))

    # --- BoC liabilities ---
    boc_circulation_notes_df = get_boc_historical_timeseries("V36625", "Notes in Circulation") * 1e6
    (DATA_DIR / "boc_circulation_notes_df.pkl").write_bytes(pickle.dumps(boc_circulation_notes_df))

    boc_goc_dollar_deposits_df = get_boc_historical_timeseries("V36628", "GoC Dollar Deposits") * 1e6
    (DATA_DIR / "boc_goc_dollar_deposits_df.pkl").write_bytes(pickle.dumps(boc_goc_dollar_deposits_df))

    boc_mop_dollar_deposits_df = get_boc_historical_timeseries("V36636", "MoP Dollar Deposits") * 1e6
    (DATA_DIR / "boc_mop_dollar_deposits_df.pkl").write_bytes(pickle.dumps(boc_mop_dollar_deposits_df))

    boc_repo_df = get_boc_historical_timeseries("V1203435186", "Repo") * 1e6
    (DATA_DIR / "boc_repo_df.pkl").write_bytes(pickle.dumps(boc_repo_df))

    boc_total_liabilities_df = get_boc_historical_timeseries("V36624", "Total Liabilities") * 1e6
    (DATA_DIR / "boc_total_liabilities_df.pkl").write_bytes(pickle.dumps(boc_total_liabilities_df))

    # --- Lynx + operations indicators ---
    bank_rate = get_boc_historical_timeseries("V39078", "Bank Rate")
    (DATA_DIR / "bank_rate.pkl").write_bytes(pickle.dumps(bank_rate))

    target_on_rate = get_boc_historical_timeseries("V39079", "Target Rate")
    (DATA_DIR / "target_on_rate.pkl").write_bytes(pickle.dumps(target_on_rate))

    operating_band_low = get_boc_historical_timeseries("V39076", "Operating Band Low Rate")
    (DATA_DIR / "operating_band_low.pkl").write_bytes(pickle.dumps(operating_band_low))

    operating_band_high = get_boc_historical_timeseries("V39077", "Operating Band High Rate")
    (DATA_DIR / "operating_band_high.pkl").write_bytes(pickle.dumps(operating_band_high))

    lynx_settlement_balance_actual = get_boc_historical_timeseries("ACTUAL", "Lynx Settlement Balances - Actual") * 1e6
    (DATA_DIR / "lynx_settlement_balance_actual.pkl").write_bytes(pickle.dumps(lynx_settlement_balance_actual))

    overnight_repo = get_boc_historical_timeseries("SPRA_OUT", "Overnight Repo") * 1e6
    (DATA_DIR / "overnight_repo.pkl").write_bytes(pickle.dumps(overnight_repo))

    overnight_rrp = get_boc_historical_timeseries("SRA_OUT", "Overnight RRP") * 1e6
    (DATA_DIR / "overnight_rrp.pkl").write_bytes(pickle.dumps(overnight_rrp))

    securities_lending = get_boc_historical_timeseries("SEC_LEND", "Securities Lending") * 1e6
    (DATA_DIR / "securities_lending.pkl").write_bytes(pickle.dumps(securities_lending))

    term_repo = get_boc_historical_timeseries("TERMREPOS", "Term Repo") * 1e6
    (DATA_DIR / "term_repo.pkl").write_bytes(pickle.dumps(term_repo))

    # --- Securities lending operations table via Valet JSON ---
    base = "https://www.bankofcanada.ca/valet"
    resp = requests.get(f"{base}/operations/securities-lending-program/json", params={"order_dir": "asc"})
    data = resp.json()

    # keep raw JSON and/or normalized table
    (DATA_DIR / "slp_raw.json").write_text(resp.text)

    # TODO: normalize to DataFrame if you want, similar to previous pattern
    # and pickle it.

    return True
