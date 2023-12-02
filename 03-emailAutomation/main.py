from dotenv import load_dotenv
from quote import Quote
from myEmail import SendEmail



def main():
    load_dotenv()
    q = Quote()
    to_email = input("Receiver's Email >>> ")
    subject = input("Subject >>> ")
    body = q.getQuote()
    e = SendEmail(to_addr = to_email, subject=subject, body = body)
    e.sendMail()

if __name__ == "__main__":
    main()