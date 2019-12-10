#step 1
from microbit import *

life = 0

while True:
    if button_a.was_pressed():
        life = life + 1
        
    display.show(life)

#step 2
from microbit import *

life = 0
radio.on()

while True:
		incoming = radio.receive()
		if incoming == "heal Sune"
				life = life + 1

    if button_a.was_pressed():
        radio.send("heal Benjamin")
        
    display.show(life)

#step 3
from microbit import *

life = 0
radio.on()

while True:
		incoming = radio.receive()
		if incoming == "heal Sune"
				life = life + 1

    if button_a.was_pressed():
        radio.send("heal Benjamin")
        
    display.show(life)