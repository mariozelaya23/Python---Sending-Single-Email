import yagmail
import os

sender = 'app7flask@gmail.com'
reveiver = 'lzykszamb@supere.ml'

subject = """
This is the subject
"""

contents = """
Here is the content of the email!
Hi!
"""

yag = yagmail.SMTP(user=sender, password=os.getenv('PASSWORD'))