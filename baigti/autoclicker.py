from pynput.mouse import Button, Controller
import time
import random
mouse = Controller()
timeslept = float(input("time: "))
time.sleep(5)
print("started")
while True:
	time.sleep(timeslept*(random.random()+.5))
	mouse.press(Button.left)
	mouse.release(Button.left)
