
import pandas as pd

datasets = {
    "fund_master": "01_fund_master.csv",
    "nav_history": "02_nav_history.csv",
    "aum": "03_aum_by_fund_house.csv",
    "sip": "04_monthly_sip_inflows.csv",
    "category": "05_category_inflows.csv",
    "folios": "06_industry_folio_count.csv",
    "performance": "07_scheme_performance.csv",
    "transactions": "08_investor_transactions.csv",
    "holdings": "09_portfolio_holdings.csv",
    "benchmark": "10_benchmark_indices.csv"
}

dfs = {}

for name, file in datasets.items():

    df = pd.read_csv(file)
    dfs[name] = df

    print("=" * 80)
    print(name.upper())

    print("\nShape:")
    print(df.shape)

    print("\nDtypes:")
    print(df.dtypes)

    print("\nHead:")
    print(df.head())

    print("\nMissing Values:")
    print(df.isnull().sum().sum())

    print("\nDuplicate Rows:")
    print(df.duplicated().sum())

print("\nData ingestion completed successfully.")
