# @author   Lucas Cardoso de Medeiros
# @since    07/12/2022
# @version  1.0

# Empire's 100 Greatest Movies Of All Time - Beautiful Soup web scrapping

from bs4 import BeautifulSoup
import requests
import random

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"


def create_list():
    response = requests.get(URL)
    web_page = response.text
    soup = BeautifulSoup(web_page, "html.parser")

    titles = [title.getText() for title in soup.find_all(name="h3", class_="title")]
    titles.reverse()

    try:
        with open(file="movies.txt", mode="w", encoding="utf-8") as file:
            for movie in titles:
                file.write(f"{movie}\n")
            print("Movie list ready! Now you have 100 new movies to watch...")
    except Exception as e:
        print('Failed to open file: ' + str(e))
        exit(-1)


def watch_movie():
    try:
        with open(file="movies.txt", mode="r", encoding="utf-8") as file:
            titles = file.readlines()
            movie = random.choice(titles)
            print(f"Today's movie is...\n   {movie}\nHave fun :)")
    except Exception as e:
        print('Failed to open file: ' + str(e))
        exit(-1)


if __name__ == "__main__":
    option = input("1 - Create movie list\n2 - Watch new movie\n")
    if option == 1:
        create_list()
    else:
        watch_movie()
