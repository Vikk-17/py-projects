import requests
from bs4 import BeautifulSoup as bs


def main():

    respons = requests.get(url="https://news.ycombinator.com/")
    yc_web_page = respons.text

    # page content
    soup = bs(yc_web_page, "html.parser")

    title_list = []
    title_links = []
    title_upvotes = []

    # find the element with span tag and class titleline
    titles = soup.find_all("span", class_="titleline")
    
    # get text and append to the title_list
    for title in titles:
        title_list.append(title.find("a").get_text())
    

    # get links and append to the title_links
    for title in titles:
        title_links.append(title.find("a").get("href"))
    

    # get votes and append to the title upvotes
    votes = soup.find_all("span", class_="score")
    for vote in votes:
        title_upvotes.append(int(vote.getText().split(" ")[0]))


    # get the maximum index from title_upvote list
    maximum = max(title_upvotes)
    maximum_index = title_upvotes.index(maximum)

    # print content correspond to the maximum upvote
    print(title_list[maximum_index])
    print(title_links[maximum_index])
    print(title_upvotes[maximum_index])



if __name__ == "__main__":
    main()