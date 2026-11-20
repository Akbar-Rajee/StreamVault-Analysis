import time
import pandas as pd

start_time = time.time()

movies = pd.read_csv("data/processed/movies.csv")

# Franchise vs standalone
summary = (
    movies
    .groupby("is_franchise")
    .agg(
        movies=("movie_id", "count"),
        avg_revenue=("revenue", "mean"),
        avg_profit=("profit", "mean"),
        avg_roi=("roi", "mean")
    )
)

# 2000+ analysis
movies_2000 = movies[movies["year"] >= 2000]

summary_2000 = (
    movies_2000
    .groupby("is_franchise")
    .agg(
        movies=("movie_id", "count"),
        avg_revenue=("revenue", "mean"),
        avg_profit=("profit", "mean"),
        avg_roi=("roi", "mean")
    )
)

# Median analysis
median_results = (
    movies
    .groupby("is_franchise")
    .agg(
        median_revenue=("revenue", "median"),
        median_profit=("profit", "median"),
        median_roi=("roi", "median")
    )
)

end_time = time.time()

print("\nRuntime:")
print(f"{end_time - start_time:.2f} seconds")