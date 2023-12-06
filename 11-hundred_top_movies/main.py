import requests
from bs4 import BeautifulSoup as bs


def main():
    respons = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
    empire_web_page = respons.text
                       
    soup = bs(empire_web_page, "html.parser")
    
    movie_list = []
    titles = soup.find_all("h3", class_="listicleItem_listicle-item__title__BfenH")
    
    for title in titles:
        movie_list.append(title.get_text())
    
    movie_list.reverse()
    
    with open("top_movies.txt", "w") as file:
        for movie in movie_list:
            file.write(f"{movie}\n")


if __name__ == "__main__":
    main()