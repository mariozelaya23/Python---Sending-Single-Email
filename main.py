import yagmail
import os
import time

sender = 'leadgeneratorsgurus@gmail.com'
receiver = 'lzykszamb@supere.ml'

subject = """
This is the subject
"""

contents = """
Here is the content of the email!
Hi!
"""
while True:
  yag = yagmail.SMTP(user=sender, password=os.getenv('PASSWORD2'))
  yag.send(to=receiver, subject=subject, contents=contents)
  print("Email Sent!")
  time.sleep(60)
