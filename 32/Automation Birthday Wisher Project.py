
import datetime as dt
import random
import smtplib

import pandas

now = dt.datetime.now()
now_tuple = (now.month, now.day)
gmail_email = "shokhrukh.jqa@gmail.com"
gmail_password = "vntv xlst xsxu rurq"

yahoo_email = "shoh_janobilov@yahoo.com"
yahoo_password = "uakq oktw swck dbie"

data = pandas.read_csv("birthdays.csv")
birthdays_to_dict = {(data_row["month"], data_row["day"]): data_row for (index,data_row) in data.iterrows()}

# data_to_dict = data.to_dict()
# print(data_to_dict)

rand_int = random.randint(1,3)


if now_tuple in birthdays_to_dict:
    bday_person = birthdays_to_dict[now_tuple]
    f_path = f"letter_{rand_int}.txt"
    with open(f_path) as letter_file:
        new_letter = letter_file.read()
        new_letter = new_letter.replace("[NAME]", bday_person["name"])

    with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
        connection.starttls()
        connection.login(user=yahoo_email, password=yahoo_password)
        connection.sendmail(
            from_addr=yahoo_email,
            to_addrs=data[data.email], msg=f"Subject:Happy Birthday!\n\n{new_letter}")






