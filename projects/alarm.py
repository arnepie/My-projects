from time import sleep
import webbrowser

alarm = 0
seconds = 0
minutes = 0
hours = 0
loop = 1000000000000000000000000000000000000000
loop_2 = 0


clock = (input("Do you want to change the time? (yes/no): "))

if clock == ("yes"):
    seconds = int(input("How many seconds? "))
    minutes = int(input("How many minutes? "))
    hours = int(input("How many hours? "))

else: 
    print("Ok!")

alarm_time = int(input("In how many minutes do you want your alarm?: "))



for i in range (loop):
    print (seconds)
    print (minutes)
    print (hours)
    print (" ")
    print (" ")
    print (" ")
    print (" ")
    print (" ")
    print (" ")
    print (" ")
    print (" ")
    print (" ")
    print (" ")
    print (" ")
    print (" ")
    print (" ")
    seconds = (seconds) + 1
    sleep(1)
    
    if (seconds) == 60:
        seconds = 0
        minutes = (minutes) + 1
        alarm = (alarm) + 1
        
    if (minutes) == 60:
        minutes = 0
        alarm = (alarm) + 1
        hours = (hours) + 1
        
    if (alarm) == (alarm_time):
        print("alarm!")
        snoozing = input("Do you wanna go into snoozing mode? (Delays the alarm with 10 minutes) (yes/no): ")
    
        if snoozing == ("yes"):
            alarm = 0
            alarm_time = 10
        
        
        if snoozing == ("no"):
            webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
                
        else: 
            print("Ok!")
        
        
    
    
