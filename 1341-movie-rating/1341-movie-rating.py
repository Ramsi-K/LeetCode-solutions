import pandas as pd

def movie_rating(movies: pd.DataFrame, users: pd.DataFrame, movie_rating: pd.DataFrame) -> pd.DataFrame:
    user_name = movie_rating.groupby(["user_id"]).agg({"movie_id": "count"}).merge(users, on="user_id").sort_values(["movie_id", "name"], ascending=[False,True])["name"].values[0]
    # print(user_name)

    movie_rating = movie_rating[(movie_rating['created_at'].dt.month==2) & (movie_rating['created_at'].dt.year==2020)]
    movie_name = movie_rating.groupby(["movie_id"]).agg({"rating": "mean"}).merge(movies, on="movie_id").sort_values(["rating", "title"], ascending=[False, True])["title"].values[0]
    # print(movie_name)

    return pd.DataFrame({"results":[user_name, movie_name]})
