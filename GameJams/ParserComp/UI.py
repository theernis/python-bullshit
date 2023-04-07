import random
import time

#amount to wait for messages
def sleep_time():
	return random.random()*1

#prints text with delay
def print1(text):
	for a in text.split("\n"):
		time.sleep(sleep_time())
		print(a)

#asks for input with delay
def input1(text):
	time.sleep(sleep_time())
	return input(text)

#prints each letter
def spell(text, speed):
	for i in range(len(text)):
		time.sleep(sleep_time() / speed)
		print(text[i], end='', flush=True)
	print("")

#prints a slider
def slider(value, max_value, size):
	time.sleep(sleep_time())
	a = int(value / max_value * size)
	b = ""
	for i in range(size):
		if a > i:
			b = b + "|"
		else:
			b = b + " "
	return "[" + b + "]"