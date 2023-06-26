
import smtplib

to = input("Enter the email of recipent:\n")

content = input("Enter the content for mail:\n")

def sendEmail(to, content):
    server = smtplib.SMTP("smtp-mail.outlook.com", 587)
    server.ehlo()
    server.starttls()
    server.login('sender@outlook.com', 'password')
    server.sendmail('sender@outlook.com', to, content)
    server.close()

sendEmail(to, content)
