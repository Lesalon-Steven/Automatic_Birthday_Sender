import smtplib
import datetime as dt
import random

my_email = ""
password = ""

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 2:
    with open("quotes.txt") as quotes:
        all_quotes = quotes.readlines()
        random_quote = random.choice(all_quotes)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="thetestman48@gmail.com",
                            msg=f"Subject:Quote\n\n{random_quote}")

