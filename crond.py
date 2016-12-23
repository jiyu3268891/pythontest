#! /usr/bin/env python
#coding=utf-8
  
import time, os 
import threading
def timer_start():
	schedule = threading.Timer(120,execute_command,())
	schedule.start()
def execute_command():
	os.system("echo hello >> /apps/adf/test/1.txt")
	timer_start()
if __name__ == "__main__":
    timer_start()
    while True:
        time.sleep(1)