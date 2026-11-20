import pandas as pd

movies = pd.read_csv("data/processed/movies.csv")
directors = pd.read_csv("data/processed/directors.csv")
actors = pd.read_csv("data/processed/actors.csv")

print("Movies table")
print("Unique movies:", movies["movie_id"].nunique())

print("\nDirectors table")
print("Unique movies:", directors["movie_id"].nunique())

print("\nActors table")
print("Unique movies:", actors["movie_id"].nunique())

print("\nRow counts")
print("Movies rows:", len(movies))
print("Director rows:", len(directors))
print("Actor rows:", len(actors))