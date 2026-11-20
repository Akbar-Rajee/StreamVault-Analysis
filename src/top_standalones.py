import pandas as pd

movies = pd.read_csv("data/processed/movies.csv")

standalones = movies[
    ~movies["is_franchise"]
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

print(standalones[cols].head(10))