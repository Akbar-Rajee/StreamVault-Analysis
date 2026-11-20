import pandas as pd

recon = pd.read_csv(
    "data/processed/reconciliation.csv"
)

recon.to_csv(
    "outputs/reconciliation_summary.csv",
    index=False
)

print("reconciliation_summary.csv created")
