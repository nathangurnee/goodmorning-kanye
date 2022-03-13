# Sends SMS messages through cell carrier
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import random
from scraper import quotes

email = # "full email address"
pswd = # "password for email account"

sms_gateway = # '<cell number>@carrier-gateway'
smtp = # "email server"
port = # port number from email provider
server = smtplib.SMTP(smtp, port)
server.starttls()
server.login(email, pswd)

body = random.choice(quotes)
server.sendmail(email, sms_gateway, body)
server.quit()