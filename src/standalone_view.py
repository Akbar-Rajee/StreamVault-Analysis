import pandas as pd

movies = pd.read_csv("data/processed/movies.csv")
actors = pd.read_csv("data/processed/actors.csv")
directors = pd.read_csv("data/processed/directors.csv")

standalone = movies[~movies["is_franchise"]]

dir_names = (
    directors.groupby("movie_id")["director"]
    .agg(", ".join)
    .rename("directors")
)

view = (
    standalone
    .merge(actors, on="movie_id", how="left")
    .merge(dir_names, on="movie_id", how="left")
    [["title", "directors", "actor", "profit"]]
    .sort_values("profit", ascending=False)
)

pd.set_option("display.width", 200)
pd.set_option("display.max_colwidth", 40)
print(view.to_string(index=False))

# Standalone benchmark with and without the named-talent films
# Director names selected from the
# highest-performing recurring director signals.

NOTABLE_DIRECTORS = [
    "Christopher Nolan",
    "Steven Spielberg",
    "Robert Zemeckis"
]
named = directors.loc[
    directors["director"].isin(
        NOTABLE_DIRECTORS
    ),
    "movie_id",
]
rest = standalone[~standalone["movie_id"].isin(named)]
print()
print("All standalone:", len(standalone), standalone["profit"].median())
print("Excluding Nolan/Spielberg/Zemeckis films:", len(rest), rest["profit"].median())
