import pandas as pd

movies = pd.read_csv("data/processed/movies.csv")

summary = (
    movies
    .groupby("is_franchise")
    .agg(
        movies=("movie_id", "count"),
        avg_revenue=("revenue", "mean"),
        avg_profit=("profit", "mean"),
        avg_roi=("roi", "mean")
    )
)

print(summary)

# Then Add the 2000+ Analysis
movies_2000 = movies[
    movies["year"] >= 2000
]

summary_2000 = (
    movies_2000
    .groupby("is_franchise")
    .agg(
        movies=("movie_id", "count"),
        avg_revenue=("revenue", "mean"),
        avg_profit=("profit", "mean"),
        avg_roi=("roi", "mean")
    )
)

print("\n2000 Onward")
print(summary_2000)