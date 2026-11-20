import pandas as pd

movies = pd.read_csv("data/processed/movies.csv")
directors = pd.read_csv("data/processed/directors.csv")
actors = pd.read_csv("data/processed/actors.csv")
reconciliation = pd.read_csv("data/processed/reconciliation.csv")

print("=== TEST RESULTS ===")

# Test 1
assert movies["movie_id"].nunique() == len(movies)
print("PASS: Movies table contains unique movie IDs")

# Test 2
assert directors["movie_id"].nunique() == movies["movie_id"].nunique()
print("PASS: No movies lost in director extraction")

# Test 3
assert actors["movie_id"].nunique() == movies["movie_id"].nunique()
print("PASS: No movies lost in actor extraction")

# Test 4
success_count = (
    reconciliation["status"] == "success"
).sum()

assert success_count == len(movies)

print(
    "PASS: Successful retrieval count matches movies table"
)

# Test 5
assert movies["profit"].notna().all()
print("PASS: Profit calculated for all movies")

print("\nAll tests passed.")