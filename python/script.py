#!/usr/bin/env python3

import webiopi
import datetime
from webiopi.devices.analog.mcp3x0x import MCP3008

GPIO = webiopi.GPIO
AUTO = True

# GPIO pin declarations using BCM numbering
P1 = 4  # Water pump relay 
S1 = 17  # Solenoid relay 1
S2 = 27 # Solenoid relay 2
S3 = 22 # Solenoid relay 3
S4 = 23 # Solenoid relay 4
S5 = 24 # Solenoid relay 5
LOWWATER = 25 # Low water switch
pins = [P1, S1, S2, S3, S4, S5]
m1 = 0
m2 = 0
m3 = 0
m4 = 0
m5 = 0

#Setup ADC
adc = MCP3008()
# ADC pin for soil moisture sensor 1 to 5
# ADC pin for light meter
# ADC pin for temperature
# ADC pin for humidity

#Variables
# ADC high and low thresholds for moisture sensors
M1LOW = 200
M1HIGH = 800
M2LOW = 0
M2HIGH = 400
M3LOW = 0
M3HIGH = 800
M4LOW = 200
M4HIGH = 400
M5LOW = 0
M5HIGH = 400
mcp = webiopi.deviceInstance("mcp") # retrieve the device named "mcp" in the configuration

# setup function is automatically called at WebIOPi startup
def setup():
	# set the GPIO direction for each pin.
	GPIO.setFunction(P1, GPIO.OUT)
	GPIO.setFunction(S1, GPIO.OUT)
	GPIO.setFunction(S2, GPIO.OUT)
	GPIO.setFunction(S3, GPIO.OUT)
	GPIO.setFunction(S4, GPIO.OUT)
	GPIO.setFunction(S5, GPIO.OUT)
	GPIO.setFunction(LOWWATER, GPIO.IN, GPIO.PUD_DOWN)


# loop function is repeatedly called by WebIOPi 
def loop():
	global mcp
	global M1LOW
	#Read in all values from all sensors
	m1 = mcp.analogRead(0)
	m2 = mcp.analogRead(1)
	m3 = mcp.analogRead(2)
	m4 = mcp.analogRead(3)
	m5 = mcp.analogRead(4)
	pump = GPIO.digitalRead(P1)
	light = mcp.analogRead(5)
	humidity = mcp.analogRead(6)
	temp = mcp.analogRead(7)
	#baro = 
	print("Zones 1:" +str(m1)+" 2:"+str(m2)+" 3:"+str(m3)+" 4:"+str(m4)+" 5:"+str(m5)+" Pump:"+str(pump)+" Light:"+str(light)+" Humidity:"+str(humidity)+" Temp:"+str(temp))

#Auto mode loop    
	if (AUTO):
		print(str(m1)+" "+str(M1LOW))
	# Check each sensor and water if required
		if (m1 < M1LOW):
			while (m1 < M1HIGH):
				if (GPIO.digitalRead(P1) == GPIO.HIGH):
					GPIO.digitalWrite(P1, GPIO.LOW)
				if (GPIO.digitalRead(S1) == GPIO.HIGH):
					GPIO.digitalWrite(S1, GPIO.LOW)
				m1 = mcp.analogRead(0)
				webiopi.sleep(1)
			GPIO.digitalWrite(P1, GPIO.HIGH)
			GPIO.digitalWrite(S1, GPIO.HIGH)
			
	# wait 15 minutes before looping again
		webiopi.sleep(1)

#Manual mode loop
#	if (AUTO == False):
	#blah

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
	global pins
	for pin in pins:
		GPIO.digitalWrite(pin, GPIO.HIGH)
    
    
