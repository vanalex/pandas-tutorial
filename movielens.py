import pandas as pd

pd.options.display.max_rows = 10

unames = ['user_id', 'gender', 'age', 'occupation', 'zip']
users = pd.read_table('./data/movielens/movies.dat', sep='::', header=None, names=unames)

rnames = ['user_id', 'movie_id', 'rating', 'timestamp']
ratings = pd.read_table('./data/movielens/ratings.dat', sep='::', header=None, names=rnames)

mnames = ['movie_id', 'title', 'genres']
movies = pd.read_table('./data/movielens/movies.dat', sep='::', header=None, names=mnames)

print('*****')
print(users[:5])
print('*****')
print(ratings[:5])
print('*****')
print(movies[:5])
