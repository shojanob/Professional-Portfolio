import smtplib

my_email = "shokhrukh.jqa@gmail.com"
password = "vntv xlst xsxu rurq"

yahoo_email = "shoh_janobilov@yahoo.com"
yahoo_password = "uakq oktw swck dbie"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="shoh_janobilov@yahoo.com", msg="Subject:Hello\n\nThis is the body of my email.")

