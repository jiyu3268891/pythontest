#!/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
import  socket
import commands
import sys
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
#from email.header import Header

mail_host="smtp.eu.jnj.com"
gridvar=sys.argv[1]

sender = 'ADF_BACKUP_MANAGER'
receivers = ['yji23@ITS.JNJ.com','zzang3@ITS.JNJ.com','wsun26@ITS.JNJ.com','wfang7@ITS.JNJ.com','ctang29@ITS.JNJ.com']
#receivers = ['ctang29@ITS.JNJ.com']
message = MIMEMultipart()
message['From'] = sender
message['To'] = "yji23@ITS.JNJ.com, zzang3@ITS.JNJ.com, wsun26@ITS.JNJ.com, wfang7@ITS.JNJ.com,ctang29@ITS.JNJ.com"
#message['To'] = "ctang29@ITS.JNJ.com"
message['Subject'] = "Bakregions failed - " + gridvar + " , please check!!! "
#text = "Bakregions failed, please check the backregions logs in the following host: \n " + "Backup server:" + hostName

html = """\
<html>
  <head></head>
  <body>
    <p>Hello All,<br>
    <br>"""+gridvar+"""
        Back regions failed. <br>
	The following is a summary information.See log file in /apps/adf/bakregions/regionbak_log/ of cluster for more information.<br><br>
    
	<span style="font-family:verdana;font-size:10px">   %s  </style></span>
	
    </p>
  </body>
</html>
"""


errlog=commands.getoutput("cat /depot/regionbaklog/bakregion_"+commands.getoutput('date "+%Y%m%d"')+".log | grep "+ gridvar +" |sort | sed '/Backup Regions begining /i\</br>=========================================================</br>' | sed '/:/a\</br>' | sed '/99:FAILED/i\<font color=#FF2D2D>' | sed '/99:FAILED/a\</font>' | sed '/99:WARNING/i\<font color=#FF8000>' | sed '/99:WARNING/a\</font>'| sed '/99:SUCCESS/i\<font color=#00A600>' | sed '/99:SUCCESS/a\</font>' " )

#part1 = MIMEText(text, 'plain')
part2 = MIMEText(html % errlog, 'html')
message.attach(part2)

try:
    smtpObj = smtplib.SMTP() 
    #smtpObj.set_debuglevel(1)
    smtpObj.connect(mail_host, 25)
    smtpObj.ehlo()
    smtpObj.starttls()
    smtpObj.ehlo
    smtpObj.sendmail(sender, receivers, message.as_string())
    smtpObj.quit()
    print "Email send successful."
except smtplib.SMTPException, ex:
    print "Error: Email send failed."
    print ex
