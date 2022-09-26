import random

from time import *

gate=True

while(gate):

    t=random.randint(0,50)

    h=random.randint(10,50)

    if t>45 and h<40:

        print("Temperature=",t,"Humidity=",h)

        print("ALARM ON")

        gate=False

    else:

        print("Temperature=",t,"Humidity=",h)

    sleep(1)