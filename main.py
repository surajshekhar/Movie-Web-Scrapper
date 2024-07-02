import requests 
from bs4 import BeautifulSoup

URL="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"


response=requests.get(URL)
web_html=response.text


soup=BeautifulSoup(web_html,"html.parser")

all_movies=soup.find_all(name="h3",class_="title")

movies_titles=[movie.getText() for movie in all_movies]
#list need to be reverse to start from 1
movies=movies_titles[::-1]
print(movies)
with open("movies.txt",mode="w",encoding="utf-8")as file:
    for movie in movies:
        file.write(f"{movie}\n")