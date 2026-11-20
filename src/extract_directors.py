import os
import json
import pandas as pd

credits_folder = "data/raw/credits"

directors = []

for file_name in os.listdir(credits_folder):

    if not file_name.endswith(".json"):
        continue

    path = os.path.join(
        credits_folder,
        file_name
    )

    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    movie_id = data.get("id")

    for crew_member in data.get("crew", []):

        if crew_member.get("job") == "Director":

            directors.append({
                "movie_id": movie_id,
                "director": crew_member.get("name")
            })

directors_df = pd.DataFrame(directors)

directors_df.to_csv(
    "data/processed/directors.csv",
    index=False
)

print(directors_df.head())
print(directors_df.shape)