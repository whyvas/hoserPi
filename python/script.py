import webiopi
import datetime

GPIO = webiopi.GPIO

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
    # retrieve current datetime
    now = datetime.datetime.now()

    # toggle light ON all days at the correct time
    if ((now.hour == HOUR_ON) and (now.minute == 0) and (now.second == 0)):
        if (GPIO.digitalRead(LIGHT) == GPIO.LOW):
            GPIO.digitalWrite(LIGHT, GPIO.HIGH)

    # toggle light OFF
    if ((now.hour == HOUR_OFF) and (now.minute == 0) and (now.second == 0)):
        if (GPIO.digitalRead(LIGHT) == GPIO.HIGH):
            GPIO.digitalWrite(LIGHT, GPIO.LOW)

    # gives CPU some time before looping again
    webiopi.sleep(1)

# destroy function is called at WebIOPi shutdown
def destroy():
    GPIO.digitalWrite(LIGHT, GPIO.LOW)
