#!/usr/local/bin/python
import smtplib
import os
from email.mime.text import MIMEText
import time
path = "/u/users/kumaran"
num_dir = len([d for d in os.listdir(path)
                if os.path.isdir(os.path.join(path, d))])
sender = 'host@example.com'
recipients = 'kumaran@example.com; preeti@example.com;'
content = "\r\n"
content += """As on """
content += time.strftime("%m/%d/%Y")
content += """, The Number of directories in /u/users/kumaran is ---> """
content += str(num_dir)
 
msg = MIMEText(content)
msg['Subject'] = "\r\n Number of directories"
msg['To'] = "kumaran@example.com; preeti@example.com;"
 
smtpserver = smtplib.SMTP("server@example.com",25)
 
try:
   smtpserver.sendmail(sender,recipients,msg.as_string())
except Exception as e:
    print "unable to send email: " ,e
finally:
    smtpserver.quit()