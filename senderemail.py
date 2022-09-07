import smtplib

import firebase_admin
import pyrebase
import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth


cred = credentials.Certificate('firebase-sdk.json')
firebase_admin.initialize_app(cred)
# password reset
email = input("Please enter your email address: \n")
link = auth.generate_password_reset_link(email, action_code_settings=None)
print(link)

gmail_user = 'careerdevelopmentdatahub@gmail.com'
gmail_password = 'Ayomipo02!'

sent_from = gmail_user
to = [str(email)]
subject = 'Password Reset'
body = str(link)

email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)

try:
    smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtp_server.ehlo()
    smtp_server.login(gmail_user, gmail_password)
    smtp_server.sendmail(sent_from, to, email_text)
    smtp_server.close()
    print("Email sent successfully!")
except Exception as ex:
    print("Something went wrong….",ex)

