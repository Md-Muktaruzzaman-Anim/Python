# go over to our gmail account and setup 2-step verification 
# generate app password
# create a function to send email

from email.message import EmailMessage
import ssl
import smtplib

email_sender = "mukatruzzamananim@gmail.com"
email_password = "zjxh cvsi yiwl cgae"

email_receiver = "jecen83249@okexbit.com"
subject = "Dont forget to subscribe"
body = """
When you watch a video, please hit like and subscribe
"""
em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())

print("Email sent successfully")