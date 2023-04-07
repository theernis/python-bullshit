from pynput.keyboard import Key, Controller
import time
keyboard = Controller()
spam = input("bot name: ")
num = input("code: ")
num1 = int(input("bot count: "))
time.sleep(5)
def write(text1):
 keyboard.press(Key.ctrl)
 keyboard.press("t")
 keyboard.release(Key.ctrl)
 keyboard.release("t")
 kah = "kahoot.it"
 for a in range(len(kah)):
  keyboard.press(kah[a])
  keyboard.release(kah[a])
 keyboard.press(Key.enter)
 keyboard.release(Key.enter)
 time.sleep(1)
 keyboard.press(Key.tab)
 keyboard.release(Key.tab)
 for a in range(len(num)):
  keyboard.press(num[a])
  keyboard.release(num[a])
 keyboard.press(Key.enter)
 keyboard.release(Key.enter)
 time.sleep(1)
 keyboard.press(Key.tab)
 keyboard.release(Key.tab)
 for a in range(len(text1)):
  keyboard.press(text1[a])
  keyboard.release(text1[a])
  if(text1[a] == " "): 
   keyboard.press(Key.space)
   keyboard.release(Key.space)
 keyboard.press(Key.enter)
 keyboard.release(Key.enter)
 time.sleep(1)
for i in range(num1):
 write(spam+"#"+str(i))
 print(spam+"#"+str(i ))
