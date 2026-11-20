import pandas as pd

recon = pd.read_csv(
    "data/processed/reconciliation.csv"
)

failed = recon[
    recon["status"] != "success"
]

print(failed)