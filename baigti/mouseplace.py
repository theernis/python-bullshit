from pynput.mouse import Button, Controller
mouse = Controller()
while 0 == 0:
    print(str(mouse.position[0]) + ", " + str(mouse.position[1]))