import time
import datetime
import sys
now = datetime.now()
n = int(input("Enter Interval"))
l = int(input("Enter No. of lines to Show at a time"))
while n!=0:
    for x in range(l):
        print ('Log Generation with respect to Time and Size', now)
    n-=1
    time.sleep(1)
