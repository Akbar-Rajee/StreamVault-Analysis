import os
import json
import time
import requests
import pandas as pd

from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("TMDB_API_KEY")

ids = pd.read_csv("data/raw/id_list.csv")

ids["tmdb_id"] = ids["tmdb_id"].astype(str)

valid_ids = ids[
    ids["tmdb_id"].str.match(r"^\d+$", na=False)
]["tmdb_id"]

valid_ids = valid_ids.drop_duplicates()
valid_ids = valid_ids.astype(int).tolist()

reconciliation = []

def get_movie_details(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}"

    return requests.get(
        url,
        params={"api_key": API_KEY},
        timeout=30
    )


def get_movie_credits(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"

    return requests.get(
        url,
        params={"api_key": API_KEY},
        timeout=30
    )


for movie_id in valid_ids:

    print(f"Processing {movie_id}")

    try:

        # DETAILS
        details_response = get_movie_details(movie_id)

        if details_response.status_code != 200:

            reconciliation.append({
    "movie_id": movie_id,
    "status": f"details_failed_{details_response.status_code}"
})

            continue

        # CREDITS
        credits_response = get_movie_credits(movie_id)

        if credits_response.status_code != 200:

            reconciliation.append({
                "movie_id": movie_id,
                "status": "credits_failed"
            })

            continue

        # SAVE DETAILS

        with open(
            f"data/raw/details/{movie_id}.json",
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                details_response.json(),
                f,
                ensure_ascii=False,
                indent=4
            )

        # SAVE CREDITS

        with open(
            f"data/raw/credits/{movie_id}.json",
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                credits_response.json(),
                f,
                ensure_ascii=False,
                indent=4
            )

        reconciliation.append({
            "movie_id": movie_id,
            "status": "success"
        })

        time.sleep(0.25)

    except Exception as e:

        reconciliation.append({
            "movie_id": movie_id,
            "status": f"error: {str(e)}"
        })

recon_df = pd.DataFrame(reconciliation)

recon_df.to_csv(
    "data/processed/reconciliation.csv",
    index=False
)

print("\nFinished")
print(recon_df["status"].value_counts())

