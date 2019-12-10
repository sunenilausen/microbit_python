#step 1
from microbit import *

tid = 0
while True:
	display.show(tid)
	sleep(1000)

#step 2
from microbit import *

while True:
	display.show(microbit.running_time() / 1000)

#step 3
from microbit import *

while True:
	if button_a.was_pressed():
		display.show(microbit.running_time() / 1000)

#step 4
from microbit import *

while True:
	if button_a.was_pressed():
		start_tid = microbit.running_time()

	if button_b.was_pressed():
		stop_tid = microbit.running_time()
		break

display.show(tidsforskel(start_tid, stop_tid)))

def tidsforskel(start, stop):
	(stop - start) / 1000