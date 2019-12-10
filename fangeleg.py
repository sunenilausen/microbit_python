#step 0
from microbit import *

while True:
    gesture = accelerometer.current_gesture()
​
    if gesture == "shake":
        display.show(Image.ANGRY)

#step 1
from microbit import *

while True:
    gesture = accelerometer.current_gesture()
​
    if gesture == "shake":
        display.show(Image.ANGRY)
    else:
        display.show(Image.HAPPY)

#step 2, MVP
from microbit import *
​
life = 1
​
while life > 0:
    gesture = accelerometer.current_gesture()
​
    if gesture == "shake":
        life = life - 1
    else:
        display.show(Image.HAPPY)
​
display.show(Image.SKULL)

#step 3
from microbit import *
​
sidste_skade = microbit.running_time()
life = 3
​
while life > 0:
    gesture = accelerometer.current_gesture()
​
    if gesture == "shake" && ikke_skadet_for_nyligt:
        life = life - 1
				sidste_skade = 0
        display.show(Image.ANGRY)
    else:
        display.show(Image.HAPPY)
​
display.show(Image.SKULL)

def ikke_skadet_for_nyligt
	nu = microbit.running_time()
	tidsforskellen = sidste_skade - nu
	tidsforskellen > 1000

#step 4
from microbit import *
​
sidste_skade = microbit.running_time()
life = 3
​
while life > 0:
    if ryster && ikke_skadet_for_nyligt:
        life = life - 1
				sidste_skade = 0
        display.show(Image.ANGRY)
    else:
        display.show(Image.HAPPY)
​
display.show(Image.SKULL)

def ikke_skadet_i(mikrosekunder)
	nu = microbit.running_time()
	tidsforskellen = sidste_skade - nu
	tidsforskellen > mikrosekunder

def ryster
	gesture = accelerometer.current_gesture()
	gesture == "shake"