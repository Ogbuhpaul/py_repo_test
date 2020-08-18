import time
import winsound
seconds = 0
minutes = 38
hours = 10
while True:
    print (str(hours) + ":" + str(minutes) + ":" + str(seconds))
    
    if seconds == 0:
        seconds = 60
        minutes = minutes - 1
        
    seconds = seconds - 1
    time.sleep(1)
    winsound.Beep(200,0)