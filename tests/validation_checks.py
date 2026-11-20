import pandas as pd

movies = pd.read_csv("data/processed/movies.csv")
directors = pd.read_csv("data/processed/directors.csv")
actors = pd.read_csv("data/processed/actors.csv")

assert movies["movie_id"].nunique() == len(movies)

assert directors["movie_id"].nunique() == (
    movies["movie_id"].nunique()
)

assert actors["movie_id"].nunique() == (
    movies["movie_id"].nunique()
)

assert movies["profit"].notna().sum() > 0

print("All validation checks passed.")