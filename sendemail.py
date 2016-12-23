#!/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = 'jiyutest'
receivers = ['yji23@ITS.JNJ.com'] 
mail_host="smtp.eu.jnj.com"
message = MIMEText('Python testchangge...', 'plain', 'utf-8')
message['From'] = Header("wow", 'utf-8')
message['To'] =  Header("jiyu", 'utf-8')

subject = 'Python SMTP SMTP TEST'
message['Subject'] = Header(subject, 'utf-8')


try:
	smtpObj = smtplib.SMTP()
	smtpObj.connect(mail_host, 25)
	smtpObj.ehlo()
	smtpObj.starttls()
	smtpObj.ehlo
	smtpObj.sendmail(sender, receivers, message.as_string())
	print "send ok"
except smtplib.SMTPException:
	print "Error: send error"