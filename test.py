import time
import datetime

n = int(input("Enter Interval"))
l = int(input("Enter No. of lines to Show at a time"))

for x in range(n):
    for x in range(l):
        now = datetime.datetime.now()
        print("Random Log Generation with time and Size input at", now)  

    time.sleep(1) 
