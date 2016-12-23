#! /usr/bin/env python
#coding=utf-8
  
import time, os 
  
def re_exe(cmd, inc): 
 while True: 
  os.system(cmd) 
  time.sleep(inc) 
  
re_exe("sh ./autobak.sh", 86400)
