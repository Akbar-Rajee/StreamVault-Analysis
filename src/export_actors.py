import pandas as pd

movies = pd.read_csv("data/processed/movies.csv")
actors = pd.read_csv("data/processed/actors.csv")

actor_movies = actors.merge(
    movies,
    on="movie_id",
    how="inner",
    validate="one_to_one"
)

summary = (
    actor_movies
    .groupby("actor")
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

summary.to_csv(
    "outputs/actor_signals.csv"
)

print("actor_signals.csv created")