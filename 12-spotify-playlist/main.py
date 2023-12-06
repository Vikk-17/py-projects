import requests
from bs4 import BeautifulSoup as bs
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

def main():
    load_dotenv()
    year = input("Year(YYYY): ")
    month = input("Month(MM): ")
    day = input("Day(DD): ")
    
    url = f"https://www.billboard.com/charts/hot-100/{year}-{month}-{day}/"
    respons = requests.get(url)
    billboard_html_page = respons.text

    # making of soup
    soup = bs(billboard_html_page, "html.parser")
    
    songs = soup.select("li ul li h3")
    song_names = [song.getText().strip() for song in songs]
    
    # print(song_names)


if __name__ == "__main__":
    main()