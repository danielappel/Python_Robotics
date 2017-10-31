from Tkinter import *
from hummingbird import Hummingbird
import time

root = Tk()

#Creates Hummingbird object 
humm = Hummingbird()


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

    a.  Turn on LED light
    s.  Start on a motor
    d.  Stop the motor
    f.  Print distances
    g.  Print temperature
    h.  Use rotary sensor
    j.  Sound Sensor
    k.  Vibration Motor
    l.  Set Servo
    space: Turn Off

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
    print "I will set the servo"
    for i in range(0,3):
        humm.set_servo(1, 0)
        time.sleep(1)
        humm.set_servo(1, 90)
        time.sleep(1)



def turn_off():
    global keep_going
    
    keep_going = False

    print "I'm turning off the hummingbird"
    humm.close()


'''
Used to tie key presses to humminbird functions
'''

def key(event):
    
    key_pressed = event.char

    if key_pressed  == "a":
        print "Setting LED to red, green and blue"
        tri_color()
    elif key_pressed == "s":
        print "Starting Gear Motor..."
        start_motor()
    elif key_pressed == "d":
        print "Stopping Gear Motor..."
        stop_motor()
    elif key_pressed == "f":
        distance_sensor()
    elif key_pressed == "g":
        temp_sensor()
    elif key_pressed == "h":
        rotary_values()
    elif key_pressed == "j":
        get_sound()
    elif key_pressed == "k":
        vibrate()
    elif key_pressed == "l":
        set_servo()
    else:
        turn_off()
        
    instructions()

def callback(event):
    frame.focus_set()
    print "clicked at", event.x, event.y



frame = Frame(root, width=100, height=100)
frame.bind("<Key>", key)
frame.bind("<Button-1>", callback)
frame.pack()

root.mainloop()

instructions()

