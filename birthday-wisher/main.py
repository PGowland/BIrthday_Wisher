import pandas
import datetime
import random
import smtplib

my_email = ("testemail@gmail.com")
to_email = ("testemal@email.org")
app_password = "eigonylugaagdfgtr"

today = datetime.datetime.now().date()
today_date = (today.day, today.month)
birthdays = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row['day'], data_row['month']): data_row for (index, data_row) in birthdays.iterrows()}

date_list = birthdays_dict.keys()

if today_date in date_list:
    letter_no = random.choice([1, 2, 3])
    letter_choice = f"letter_templates/letter_{letter_no}.txt"
    l = open(letter_choice, 'r')
    letter = l.read()
    named_letter = letter.replace("[NAME]", birthdays_dict[today_date]['name'])
    print(named_letter)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=app_password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=to_email,
                            msg=f"Subject:Happy Birthday\n\n{named_letter}")
