import pandas as pd

movies = pd.read_csv("data/processed/movies.csv")
actors = pd.read_csv("data/processed/actors.csv")
directors = pd.read_csv("data/processed/directors.csv")

actor_df = actors.merge(movies, on="movie_id", validate="one_to_one")
director_df = directors.merge(movies, on="movie_id", validate="many_to_one")


def split(df, name):
    overall = df.groupby(name).agg(
        films=("movie_id", "count"),
        franchise_films=("is_franchise", "sum"),
        median_profit=("profit", "median"),
    )
    standalone = (
        df[~df["is_franchise"]]
        .groupby(name)["profit"]
        .agg(standalone_films="count", standalone_median_profit="median")
    )
    out = overall.join(standalone).fillna(0)
    out = out[out["films"] >= 2]
    return out.sort_values("median_profit", ascending=False)


pd.set_option("display.width", 200)
print("ACTORS")
print(split(actor_df, "actor").head(20))
print()
print("DIRECTORS")
print(split(director_df, "director").head(20))
