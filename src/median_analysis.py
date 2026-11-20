import pandas as pd

movies = pd.read_csv("data/processed/movies.csv")

summary = (
    movies
    .groupby("is_franchise")
    .agg(
        median_revenue=("revenue", "median"),
        median_profit=("profit", "median"),
        median_roi=("roi", "median")
    )
)

print(summary)