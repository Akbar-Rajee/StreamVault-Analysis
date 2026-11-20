import os
import json
import pandas as pd

details_folder = "data/raw/details"

movies = []

for file_name in os.listdir(details_folder):

    if not file_name.endswith(".json"):
        continue

    path = os.path.join(details_folder, file_name)

    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    movies.append({
        "movie_id": data.get("id"),
        "title": data.get("title"),
        "release_date": data.get("release_date"),
        "budget": data.get("budget"),
        "revenue": data.get("revenue"),
        "runtime": data.get("runtime"),
        "popularity": data.get("popularity"),
        "vote_average": data.get("vote_average"),
        "vote_count": data.get("vote_count"),
        "collection_id": (
            data.get("belongs_to_collection", {})
            .get("id")
            if data.get("belongs_to_collection")
            else None
        ),
        "collection_name": (
            data.get("belongs_to_collection", {})
            .get("name")
            if data.get("belongs_to_collection")
            else None
        )
    })

movies_df = pd.DataFrame(movies)

movies_df["profit"] = (
    movies_df["revenue"] -
    movies_df["budget"]
)

# Avoid Division by Zero
import numpy as np

movies_df["roi"] = np.where(
    movies_df["budget"] > 0,
    movies_df["profit"] / movies_df["budget"],
    np.nan
)

# Create Franchise Flag
movies_df["is_franchise"] = (
    movies_df["collection_id"]
    .notna()
)

# Create Release Year
movies_df["year"] = pd.to_datetime(
    movies_df["release_date"]
).dt.year


movies_df.to_csv(
    "data/processed/movies.csv",
    index=False
)

print(movies_df.shape)
print(movies_df.head())