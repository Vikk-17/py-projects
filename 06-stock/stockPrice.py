from dotenv import load_dotenv
import os
import requests


# get stock price form alpha vantage https://www.alphavantage.co/

def price() -> tuple:
    load_dotenv()
    response = requests.get(os.getenv("url"))
    data = response.json()
    today = data["Time Series (Daily)"]["2023-11-30"]["4. close"]
    yesterday = data["Time Series (Daily)"]["2023-11-29"]["4. close"]
    return (yesterday, today)


def percentage() -> str:
    y, t = price()
    yesterday = float(y)
    today = float(t)

    if yesterday > today:
        percentage = ((yesterday-today)/yesterday) * 100
        return f"{percentage:.2f}% decrease in Tesla(TSLA) stocks"
    elif yesterday < today:
        percentage = ((today-yesterday)/yesterday) * 100
        return f"{percentage:.2f}% increase in Tesla(TSLA) stocks"


# print(percentage())