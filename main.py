import yagmail
import os

sender = 'leadgeneratorsgurus@gmail.com'
receiver = 'lzykszamb@supere.ml'

subject = """
This is the subject
"""

contents = """
Here is the content of the email!
Hi!
"""

yag = yagmail.SMTP(user=sender, password=os.getenv('PASSWORD2'))
yag.send(to=receiver, subject=subject, contents=contents)
print("Email Sent!")
