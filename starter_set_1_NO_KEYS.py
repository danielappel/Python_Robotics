
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

#The following functions are tied to key presses

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
    humm.set_tricolor_led(1, 0, 255, 0)
    time.sleep(1)
    humm.set_tricolor_led(1, 0, 0, 255)

def start_motor():
    humm.set_motor(1, 255)

def stop_motor():
    humm.set_motor(1, 0)
    
def distance_sensor():
     #Loop until object <20cm away detected
     distance = humm.get_distance(2)
     print "I will print the distance for the next 5 seconds"
     start = time.time()

     stop = start + 5
    
     while(start < stop):
        print "Distance: ", humm.get_distance(2)
        start = time.time()

def temp_sensor():
    temp = humm.get_temperature(1)
    print "The temperature is", temp


def rotary_values():
    rotary = humm.get_knob_value(3)

    while(rotary !=0):
        print "Rotary value:", rotary
        rotary = humm.get_knob_value(3)

def get_sound():
    print "I will record the sound levels for the next 5 seconds"
    start = time.time()

    stop = start + 5
    
    while(start < stop):
        print "Sound level: ", humm.get_sound_sensor(4)
        start = time.time()

def vibrate():
    #Vibrate 5 times
    for i in range(0,5):
        humm.set_vibration_motor(1, 255)
        time.sleep(1)
        humm.set_vibration_motor(1, 0)
        time.sleep(1)

def set_servo():
    for i in range(0,3):
        humm.set_servo(1, 0)
        time.sleep(1)
        humm.set_servo(1, 90)
        time.sleep(1)

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

