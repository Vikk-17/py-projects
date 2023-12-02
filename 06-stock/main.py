from stockPrice import percentage
from news import getNews
import os
from twilio.rest import Client
from dotenv import load_dotenv

def main():
    load_dotenv()

    news1, news2 = getNews()
    
    # news1
    news1_title = news1[0]
    news1_description = news1[1]
    news1_url = news1[2]

    # news2
    news2_title = news2[0]
    news2_description = news2[1]
    news2_url = news2[2]

    # get the percentage_value
    petcent = percentage()

    msg_body = f"\n{petcent}\n\nHeadlines:\nID:01\n{news1_title}\n{news1_description}\n{news1_url}\n\nID:02\n{news2_title}\n{news2_description}\n{news2_url}"

    account_sid = os.getenv("TWILIO_ACCOUNT_SID")
    auth_token = os.getenv("TWILIO_AUTH_TOKEN")
    client = Client(account_sid, auth_token)

    message = client.messages.create(
                                from_="+19044743343",
                                body=msg_body,
                                to="+918240190627"
                            )

    print("Sent...")


if __name__ == "__main__":
    main()