from sqlite3 import *
# con = mysql.connector.connect(user='root',password='',host='localhost',database = '')
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

email = 'bookportal.tk@gmail.com'
password= 'Atfu2244'
msg = MIMEMultipart()
msg['from'] = "bzohab@gmail.com"
msg['to'] = "tehreemmughal341@gmail.com"

msg['subject'] = "Test Email Check Again"

file = open('open.html')
body = file.read()

msg.attach(MIMEText(body,'html'))
print(msg)


server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(email,password)
server.sendmail(msg['from'],msg['to'],msg.as_string())
server.quit()



# class Umer():
#     def __init__(self):
#         self.__content = None
#
#     def setContent(self, content):
#         self.__content = content
#
#     def getContent(self):
#         return self.__content
#
#
# a = Umer()
# a.setContent("Tariq")
# print(a.getContent())
