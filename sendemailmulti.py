#!/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
sender = 'jiyutest'
receivers = ['yji23@ITS.JNJ.com'] 
mail_host="smtp.eu.jnj.com"
message = MIMEMultipart()
message['From'] = Header("菜鸟教程", 'utf-8')
message['To'] =  Header("给自己看的东西", 'utf-8')
subject = 'Python SMTP SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')
message.attach(MIMEText('这是菜鸟教程Python 邮件发送测试……', 'plain', 'utf-8'))
att1 = MIMEText(open('1.txt', 'rb').read(), 'base64', 'utf-8')
att1["Content-Type"] = 'application/octet-stream'
att1["Content-Disposition"] = 'attachment; filename="test.txt"'
message.attach(att1)

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