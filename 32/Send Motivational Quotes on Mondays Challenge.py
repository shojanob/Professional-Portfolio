import datetime as dt
import random
import smtplib

now = dt.datetime.now()
weekday = now.weekday()

gmail_email = "shokhrukh.jqa@gmail.com"
gmail_password = "vntv xlst xsxu rurq"

yahoo_email = "shoh_janobilov@yahoo.com"
yahoo_password = "uakq oktw swck dbie"

if weekday == 0:
    with open("quotes.txt") as quotes:
        quote_txt = quotes.readlines()

    with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
        connection.starttls()
        connection.login(user=yahoo_email, password=yahoo_password)
        connection.sendmail(
            from_addr=yahoo_email,
            to_addrs=gmail_email, msg=f"Subject:Motivation Monday\n\n{random.choice(quote_txt)}")