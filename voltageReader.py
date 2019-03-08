import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library

def input_callback1(channel):
    print("1")
    
def input_callback0(channel):
    print("0")
    
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
if temp == 0:
    GPIO.add_event_detect(10,GPIO.RISING,callback=input_callback1) # Setup event on pin 10 rising edge
else:
    GPIO.add_event_detect(10,GPIO.FALLING,callback=input_callback0) # Setup event on pin 10 rising edge

## Setup the GPIO for PWM on pin12 {GPIO18}
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)
p = GPIO.PWM(12, 20000000)
p.start

message = input("Press enter to quit\n\n") # Run until someone presses enter
GPIO.cleanup() # Clean up
