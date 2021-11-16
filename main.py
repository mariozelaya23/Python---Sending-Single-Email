import yagmail
import os
import pandas

sender = 'leadgeneratorsgurus@gmail.com'

yag = yagmail.SMTP(user=sender, password=os.getenv('PASSWORD2'))

df = pandas.read_csv('contacts.csv')

def generate_file(filename, content):
  with open(filename, 'w') as file:
    file.write(str(content))

for index, row in df.iterrows():
  name = row['name']
  filename = name + ".txt"
  amount = row['amount']
  receiver_email = row['email']

  generate_file(filename, amount)
  
  subject = "This is the subject"
  contents = [f"""Hi, {name} you have to pay {amount}
  bill is attached""", filename,]

  yag.send(to=receiver_email, subject=subject, contents=contents)
  print("Email Sent!")

