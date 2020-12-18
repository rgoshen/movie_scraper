import requests
from bs4 import BeautifulSoup

URL = "https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)

eo_webpage = response.text

soup = BeautifulSoup(eo_webpage, 'html.parser')

all_movies = soup.find_all(name="h3", class_="title")
movies_titles = [movie.getText() for movie in all_movies]

movies = movies_titles[::-1]

with open("movies.txt", mode="w") as file:
    for movie in movies:
        file.write(f"{movie}\n")
