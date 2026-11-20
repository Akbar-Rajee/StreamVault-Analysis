import pandas as pd

movies = pd.read_csv("data/processed/movies.csv")

directors = pd.read_csv(
    "data/processed/directors.csv"
)

director_movies = directors.merge(
    movies,
    on="movie_id",
    how="inner",
    validate="many_to_one"
)

summary = (
    director_movies
    .groupby("director")
    .agg(
        films=("movie_id", "count"),
        avg_profit=("profit", "mean"),
        avg_revenue=("revenue", "mean"),
        avg_roi=("roi", "mean")
    )
)

summary = summary[
    summary["films"] >= 2
]

summary = summary.sort_values(
    by="avg_profit",
    ascending=False
)

print(summary.head(20))