
from hummingbird import Hummingbird
import time



#Creates Hummingbird object 
humm = Hummingbird()

#Global Variables
keep_going = True

'''
Hummingbird Hardware Components

Connect TriColor LED to Port #1
Connect Servo Motor to port #1
Connect Gear Motor to port #1
Connect Temperature Sensor to sensor port #1
Connect Distance Sensor to sensor port #2
Connect Rotary Sensor to sensor port #3
Connect Sound Sensor to sensor port #4

'''

#The following functions are tied to numeric entries

def instructions():

    print """

    Welcome to my hummingbird:

    1.  Turn on LED light
    2.  Start on a motor
    3.  Stop the motor
    4.  Print distances
    5.  Print temperature
    6.  Use rotary sensor
    7.  Sound Sensor
    8.  Vibration Motor
    9.  Set Servo
    10. Turn Off

    """


def tri_color():
    #Set LED in port 1 to red
    humm.set_tricolor_led(1, 255, 0, 0)
    time.sleep(1)
    #Set LED in port 1 to green
    time.sleep(1)
    #Set LED in port 1 to blue

def start_motor():
    #Set motor in port 1 to max speed
    humm.set_motor(1, 1)
    time.sleep(1)
    #set motor in port 1 to low speed
    
    #set motor in port 1 to max reverse speed
    

def stop_motor():
    #Stop the motor on port #1
    humm.set_motor(1, 0)
    
def distance_sensor():
     #Print the distances from the distance sensor for 5 seconds
     distance = humm.get_distance(2)
     print "I will print the distance for the next 5 seconds"
     start = time.time()

     stop = start + 5
    
     while(start < stop):
        print "Distance: ", humm.get_distance(2)
        start = time.time()

     #Create a while loop that will print the distance until the distance is below 10cm
     

def temp_sensor():
    temp = humm.get_temperature(1)

    #print the temperature for the next 5 seconds


def rotary_values():
    rotary = humm.get_knob_value(3)

    #Create a loop that will print the rotary values until a rotary value of 0 is met
    

def get_sound():
    #Create a loop that prints the sound levels for the next 5 seconds
    pass
    
def vibrate():
    #Make the vibration motor vibrate for 1 second, repeat this 5 times

    humm.set_vibration_motor(1, 255)
    

def set_servo():
    #Set the servo to 0, wait 1 second and set it to 90.  Do this three times
    humm.set_servo(1, 0)


    #Set the position of the servo motor to the rotary sensor value (think about how you will exit this loop)
    
        

def get_user_choice():
    
    choice = int(input("What is your choice? (enter 1-9)"))

    if choice == 1:
        tri_color()
    elif choice == 2:
        start_motor()
    elif choice == 3:
        stop_motor()
    elif choice == 4:
        distance_sensor()
    elif choice == 5:
        temp_sensor()
    elif choice == 6:
        rotary_values()
    elif choice == 7:
        get_sound()
    elif choice == 8:
        vibrate()
    elif choice == 9:
        set_servo()
        
    else:
        turn_off()
        

def turn_off():
    global keep_going
    
    keep_going = False

    print "I'm turning off the hummingbird"
    humm.close()

def main():
    
    while(keep_going):
        instructions()
        get_user_choice()
        

    

main()

