import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv

from config.config import TEMPLATE

def send_email(email):

    load_dotenv()

    email_from = os.getenv('smtp_username')
    email_from_pass = os.getenv('smtp_password')
    email_to = email

    sendler = MIMEMultipart('alternative')
    sendler['Subject'] = "Продукты от топового банка России"
    sendler['From'] = email_from
    sendler['To'] = email_to

    with open(TEMPLATE, encoding='utf-8') as f:
        html = f.read()

    part2 = MIMEText(html, 'html')

    sendler.set_payload(part2)

    s = smtplib.SMTP_SSL(os.getenv('smtp_server'), 465)

    s.login(email_from, email_from_pass)
    s.sendmail(email_from, email_to, sendler.as_string())
    s.quit()
