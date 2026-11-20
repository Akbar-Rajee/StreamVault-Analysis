import pandas as pd

movies = pd.read_csv("data/processed/movies.csv")

movies = movies[
    movies["year"] >= 2000
]

franchises = movies[
    movies["is_franchise"] == True
]

summary = (
    franchises
    .groupby("collection_name")
    .agg(
        titles=("movie_id", "count"),
        avg_revenue=("revenue", "mean"),
        avg_profit=("profit", "mean"),
        avg_roi=("roi", "mean")
    )
)

summary = summary[
    summary["titles"] >= 3
]

summary = summary.sort_values(
    by="avg_profit",
    ascending=False
)

print(summary)