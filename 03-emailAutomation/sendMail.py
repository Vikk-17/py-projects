# function based

from smtplib import SMTP
from email.message import EmailMessage
from dotenv import load_dotenv
import os
import random
from datetime import datetime


# take env variabes from .env file
load_dotenv()

smtpDomain = "smtp.gmail.com"
smtpPort = 587


# user data
userEmail = os.getenv("userEmail")
userPassword = os.getenv("userPassword")

def main() -> None:
    if getWeekday() == 3:
        motivation = getQuote()
        sendMail(motivation)


def getWeekday() -> int:
    now = datetime.now()
    wday = now.isoweekday()
    return wday


def getQuote() -> str:
    with open("quotes.txt") as file:
        quotes = list()
        data = file.readlines()
        for lines in data:
            quotes.append(lines.rstrip())
        return random.choice(quotes)


def sendMail(q:str) -> None:
    msg = EmailMessage()
    msg["From"] = userEmail
    msg["To"] = "downeyjr0000@gmail.com"
    msg["Subject"] = "Motivation"
    msg.set_content(q)
    
    with SMTP(smtpDomain, smtpPort) as mail:

        # TLS support
        mail.starttls()

        # login
        mail.login(user=userEmail, password=userPassword)
        mail.send_message(msg)

if __name__ == "__main__":
    main()