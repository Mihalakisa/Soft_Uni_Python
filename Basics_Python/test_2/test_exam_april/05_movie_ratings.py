import sys

movie_number = int(input())
max_rating = -sys.maxsize
min_rating = sys.maxsize
average_rating = 0

for i in range(movie_number):
    movie_name = input()
    movie_rating = float(input())
    average_rating += movie_rating

    if movie_rating > max_rating:
        max_rating = movie_rating
        movie_high = movie_name

    if movie_rating < min_rating:
        min_rating = movie_rating
        movie_low = movie_name

average_rating /= movie_number
print(f"{movie_high} is with highest rating: {max_rating:.1f}")
print(f"{movie_low} is with lowest rating: {min_rating:.1f}")
print(f"Average rating: {average_rating:.1f}")