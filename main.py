import yagmail
import os
import pandas


sender = 'leadgeneratorsgurus@gmail.com'

"""
receiver = 'lzykszamb@supere.ml'
"""

subject = """
This is the subject
"""

yag = yagmail.SMTP(user=sender, password=os.getenv('PASSWORD2'))

df = pandas.read_csv('contacts.csv')
#print(df)

for index, row in df.iterrows():
    contents = f"""Hi {row['name']} Here is the content of the email!"""
    yag.send(to=row['email'], subject=subject, contents=contents)
    print("Email Sent!")

"""
while True:
  now = dt.now()
  if now.hour == 13 and now.minute == 18: 
    yag = yagmail.SMTP(user=sender, password=os.getenv('PASSWORD2'))
    yag.send(to=receiver, subject=subject, contents=contents)
    print("Email Sent!")
    time.sleep(60)
"""