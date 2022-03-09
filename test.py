import time
n = int(input("Enter Interval"))
while n!=0:
    try:
        print ('Random Log')
        time.sleep(1)
        n-=1
    except:
        print("Error")
