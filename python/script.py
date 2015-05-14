import webiopi
import datetime

GPIO = webiopi.GPIO
AUTO = True

# GPIO pin declarations using BCM numbering
P1 = 0  # Water pump relay 
S1 = 1  # Solenoid relay 1
S2 = 4  # Solenoid relay 2
S3 = 17 # Solenoid relay 3
S4 = 21 # Solenoid relay 4
S5 = 22 # Solenoid relay 5
LOWWATER = 10 # Low water switch
# ADC pin for soil moisture sensor 1 to 5
# ADC pin for light meter
# ADC pin for temperature
# ADC pin for humidity

#Variables
# ADC high and low thresholds for moisture sensors
M1LOW = 0
M1HIGH = 0
M2LOW = 0
M2HIGH = 0
M3LOW = 0
M3HIGH = 0
M4LOW = 0
M4HIGH = 0
M5LOW = 0
M5HIGH = 0





# setup function is automatically called at WebIOPi startup
def setup():
    # set the GPIO direction for each pin.
GPIO.setFunction(P1, GPIO.OUT)
GPIO.setFunction(S1, GPIO.OUT)
GPIO.setFunction(S2, GPIO.OUT)
GPIO.setFunction(S3, GPIO.OUT)
GPIO.setFunction(S4, GPIO.OUT)
GPIO.setFunction(S5, GPIO.OUT)
GPIO.setFunction(LOWWATER, GPIO.IN)

# loop function is repeatedly called by WebIOPi 
def loop():
    #Read in all values from all sensors
    m1 = 
    m2 = 
    m3 = 
    m4 = 
    m5 = 
    pump = GPIO.digitalRead(P1)
    light = 
    humidity =
    temp =
    baro = 

#Auto mode loop    
    if (AUTO):
        # Check each sensor and water if required
        if (m1 =< M1LOW) ):
            while (m1 =< M1HIGH):
                if (GPIO.digitalRead(S1) == GPIO.HIGH):
                    GPIO.digitalWrite(S1, GPIO.LOW)
                    sleep(5)
            GPIO.digitalWrite(S1, GPIO.HIGH)



        # wait 15 minutes before looping again
        webiopi.sleep(900)
#Manual mode loop
    elif



#macros for javascript         
@webiopi.macro
def getMode():
    if (AUTO):
        return "auto"
    return "manual"

@webiopi.macro
def setMode(mode):    
    global AUTO
    if (mode == "auto"):
        AUTO = True
    elif (mode == "manual"):
        AUTO = False
    return getMode()
    
# Turn off all pumps and solenoids when exiting.
def destroy():
    GPIO.digitalWrite(P1, GPIO.HIGH)
    GPIO.digitalWrite(S1, GPIO.HIGH)
    GPIO.digitalWrite(S2, GPIO.HIGH)
    GPIO.digitalWrite(S3, GPIO.HIGH)
    GPIO.digitalWrite(S4, GPIO.HIGH)
    GPIO.digitalWrite(S5, GPIO.HIGH)
    
    
