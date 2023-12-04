import requests
from bs4 import BeautifulSoup as bs

def main():
    respons = requests.get(url="https://news.ycombinator.com/")
    yc_web_page = respons.text
    soup = bs(yc_web_page, "html.parser")
    titleLine = soup.find("span", class_="titleline")
    print(titleLine)


if __name__ == "__main__":
    main()