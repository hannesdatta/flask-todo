import smtplib
import os
from email.mime.text import MIMEText

# initialize connection to our email server, we will use Outlook here
def send_mail(receiver_email, subject, message):
    sender_noreply = 'no-reply@datta-online.com'
    smtp = smtplib.SMTP('smtp.ionos.de', port='587')
    smtp.ehlo()  # send the extended hello to our server
    smtp.starttls()  # tell server we want to communicate with TLS encryption
    smtp.login('tilburg-pulse@datta-online.com', os.getenv('TSH_EMAIL_PASSWORD')) # login to our email server
    # send our email message
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = sender_noreply
    msg['To'] = receiver_email
    smtp.sendmail('tilburg-pulse@datta-online.com',
                  receiver_email,
                  msg.as_string())
    smtp.quit()  # finally, don't forget to close the connection
