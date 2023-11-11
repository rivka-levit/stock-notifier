"""
Send emails classes.
"""

import os
import ssl
import smtplib
from email.message import EmailMessage

from dotenv import load_dotenv

load_dotenv()


class EmailTrendNotification:
    """Mail notification when the trend changes."""

    def __init__(self):
        self.sender = os.environ.get('SENDER_EMAIL')
        self.password = os.environ.get('SENDER_PASS')
        self.receiver = os.environ.get('RECEIVER_EMAIL')

    def send(self, tend_value):
        """Send email when the trend changes."""

        msg = EmailMessage()
        msg['Subject'] = 'Zagreb Stock Exchange Notification'
        msg['From'] = self.sender
        msg['To'] = self.receiver
        msg.set_content(f"Hi! The CBX trend has reached the level you waited. "
                        f"By now it is {tend_value}")

        context = ssl.create_default_context()

        with smtplib.SMTP('smtp.office365.com', 587) as server:
            server.starttls(context=context)
            server.login(self.sender, self.password)
            server.sendmail(self.sender, self.receiver, msg.as_string())


if __name__ == '__main__':
    mail = EmailTrendNotification()
    mail.send(-0.15)
