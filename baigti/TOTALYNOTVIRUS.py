from pynput.mouse import Button, Controller
mouse = Controller()
x = mouse.position[0]
y = mouse.position[1]
while 0 == 0:
    mouse.position = (x, y)