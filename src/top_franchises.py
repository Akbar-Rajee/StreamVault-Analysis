import pandas as pd

movies = pd.read_csv("data/processed/movies.csv")

franchise_movies = movies[
    movies["is_franchise"] == True
]

franchise_summary = (
    franchise_movies
    .groupby("collection_name")
    .agg(
        titles=("movie_id", "count"),
        avg_revenue=("revenue", "mean"),
        avg_profit=("profit", "mean"),
        avg_roi=("roi", "mean")
    )
    .sort_values(
        by="avg_profit",
        ascending=False
    )
)

print(franchise_summary.head(15))