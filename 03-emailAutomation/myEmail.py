import os
from email.message import EmailMessage
from smtplib import SMTP

class SendEmail:
    """
    Send email using smtp protocol
    """

    __smtpDomain = "smtp.gmail.com"
    __smtpPort = 587

    def __init__(self, to_addr:str, subject:str, body:str) -> None:
        self.to_addr = to_addr
        self.subject = subject
        self.body = body

        self.email = os.getenv("userEmail") # your email
        self.password = os.getenv("userPassword") # your password
    

    def sendMail(self) -> None:
        msg = EmailMessage()
    
        msg["From"] = self.email
        msg["To"] = self.to_addr
        msg["Subject"] = self.subject
        msg.set_content(self.body)

        with SMTP(self.__smtpDomain, self.__smtpPort) as mail:

            # TLS support
            mail.starttls()

            # login
            mail.login(user=self.email, password=self.password)
            mail.send_message(msg)




