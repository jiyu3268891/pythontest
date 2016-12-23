#! /usr/bin/env python
#coding=utf-8
  
import paramiko
import sys 
file=open("ip.list", "r") 
port=22
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
	s.connect(host,port,username,password) 
	stdin,stdout,sterr=s.exec_command("df -hl") 
	print stdout.read() 
	s.close()
file.close()

