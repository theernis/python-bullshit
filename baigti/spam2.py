from pynput.keyboard import Key, Controller
import time
keyboard = Controller()
spam = input("spam input: ")
spamsleep = float(input("spam sleep: "))
spamamount = int(input("spam sleep: "))
time.sleep(5)
inta = 0
def write(text1):
 for a in range(len(text1)):
  keyboard.press(text1[a])
  keyboard.release(text1[a])
  if(text1[a] == " "): 
   keyboard.press(Key.space)
   keyboard.release(Key.space)
 keyboard.press(Key.enter)
 keyboard.release(Key.enter)
 print(text1)
 time.sleep(spamsleep)
for i in range(spamamount):
 write(spam)
