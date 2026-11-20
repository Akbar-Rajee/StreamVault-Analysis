import pandas as pd

movies = pd.read_csv("data/processed/movies.csv")

standalones = movies[
    movies["is_franchise"] == False
]

standalones = standalones.sort_values(
    by="profit",
    ascending=False
)

cols = [
    "title",
    "year",
    "revenue",
    "profit",
    "roi"
]

standalones[cols].to_csv(
    "outputs/standalone_rankings.csv",
    index=False
)

print("standalone_rankings.csv created")