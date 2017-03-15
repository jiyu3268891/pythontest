#! /usr/bin/env python
#coding=utf-8
import paramiko
import sys
import os
f = open('file.txt', 'wb+')
sys.stdout = f

file = open("ip.list", "r") 
port = 22
for line in file.readlines():
	if line[0:1] == '#': continue
	line = line.strip('\n')
	items = line.split()
	port = 22
	host = items[0]
	username = items[1]
	password = items[2]
	s=paramiko.SSHClient() 
	s.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
	try:
		s.connect(host,port,username,password) 
	except Exception, e:		
		print host,"SSH negotiation failed.",password,"is not correct"
	else:
		print host,"SSH connect is success.",password,"is correct"
	s.close()
file.close()
f.close()
os.system("cat file.txt | grep failed | awk '{print $1}'> errorhost.txt")
os.system("cat file.txt | grep success | awk '{print $1,$6}'> righthost.txt")