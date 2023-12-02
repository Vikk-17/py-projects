from newsapi import NewsApiClient

# news api https://newsapi.org/

def getNews():
    newsapi = NewsApiClient(api_key='6c0c11e5e19b4c12a00ea20b10eae2cd')

    all_articles = newsapi.get_everything(q='Tesla',
                                        from_param='2023-11-30',
                                        language='en',
                                        sort_by='relevancy')
    title1 = [all_articles["articles"][0]["title"], all_articles["articles"][0]["description"], all_articles["articles"][0]["url"]]
    title2 = [all_articles["articles"][1]["title"], all_articles["articles"][1]["description"], all_articles["articles"][1]["url"]]

    return (title1, title2)

def main():
    
    print(getNews())

if __name__ == "__main__":
    main()