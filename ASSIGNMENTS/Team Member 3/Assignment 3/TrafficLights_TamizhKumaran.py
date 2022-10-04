from gpiozero import LED 
from time import sleep
green = LED (5)
red = LED (6) 
blue = LED (13)
while True:
	green.off() 
	red.off()
	blue.off() 
	sleep (4)
	green.on() 
	sleep(4)
	green.off() 
	red.on()
	sleep(4)
	red.off() 
	blue.on()
	sleep(4)