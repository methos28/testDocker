import time
import sys
n = int(sys.argv[1])
while n!=0:
    try:
        print ('Random Log')
        time.sleep(1)
        n-=1
    except:
        print("Error")
