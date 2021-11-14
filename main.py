import yagmail
import os
import pandas


sender = 'leadgeneratorsgurus@gmail.com'

yag = yagmail.SMTP(user=sender, password=os.getenv('PASSWORD2'))

df = pandas.read_csv('contacts.csv')
#print(df)

for index, row in df.iterrows():
  receiver_email = row['email']
  subject = "This is the subject"
  contents = [f"""Hi, {row['name']} you have to pay {row['amount']}
  bill is attached""", row['filepath'],]
  yag.send(to=row['email'], subject=subject, contents=contents)
  print("Email Sent!")

