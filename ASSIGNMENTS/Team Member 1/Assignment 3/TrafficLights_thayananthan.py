from gpiozero import LED 
from time import sleep
green = LED (5)
red = LED (6) 
blue = LED (13)
while True:
	green.off() 
	red.off()
	blue.off() 
	sleep (2)
	green.on() 
	sleep(2)
	green.off() 
	red.on()
	sleep(2)
	red.off() 
	blue.on()
	sleep(2)