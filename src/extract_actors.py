import os
import json
import pandas as pd

credits_folder = "data/raw/credits"

actors = []

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

    cast = data.get("cast", [])

    # Lead actor = first billed actor

    actor_name = None

    if len(cast) > 0:
        actor_name = cast[0]["name"]

    actors.append({
        "movie_id": movie_id,
        "actor": actor_name
    })

actors_df = pd.DataFrame(actors)

actors_df.to_csv(
    "data/processed/actors.csv",
    index=False
)

print(actors_df.head())
print(actors_df.shape)
