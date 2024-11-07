# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 08:50:35 2024

@author: Acer
"""

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
import getpass

# SMTP_SERVER = 'aspmx.1.google.com'
SMTP_SERVER = 'smtp.gmail.com'
# SMTP_PORT = 25 #587
SMTP_PORT = 587

def send_email(sender,receipt):
    msg = MIMEMultipart()
    msg['To']= receipt
    msg['From'] = sender
    subject = input("enter subject")
    msg['Subject'] = subject
    message = input('Email content: ')
    part = MIMEText('text','plain')
    part.set_payload(message)
    msg.attach(part)

    # create smtp session
    session = smtplib.SMTP(SMTP_SERVER,SMTP_PORT)
    session.set_debuglevel(1)
    session.ehlo()
    session.starttls()
    session.ehlo()
    password = getpass.getpass()
    session.login(sender,password)
    #send 
    session.sendmail(sender, receipt, msg.as_string())
    print("your email is send to {0}" .format(receipt))
    session.quit()
    
if __name__ == '__main__':
    sender = input('From address:')
    receipt = input("To address: ")
    send_email(sender, receipt)