import os
import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("TMDB_API_KEY")

movie_id = 550

response = requests.get(
    f"https://api.themoviedb.org/3/movie/{movie_id}",
    params={"api_key": api_key}
)

print(response.status_code)

if response.status_code == 200:
    movie = response.json()
    print(movie["title"])
else:
    print(response.text)