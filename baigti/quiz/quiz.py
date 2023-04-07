import random
import os

questions_string = open(input("filename: "), "r").read()

questions = questions_string.split("\n")
random.shuffle(questions)

score = 0

def Ask(question):
	answer = input(question.split(" - ")[0] + " - ")
	if (answer.lower() == question.split(" - ")[1].lower()):
		print("--correct")
		return 1
	print("--incorrect, correct was: " + question.split(" - ")[1].lower())
	return 0

for question in questions:
	score += Ask(question)

print(int(score / len(questions) * 10))

os.system('pause')