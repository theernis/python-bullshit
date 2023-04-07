storedats = []
print("simboliai:")
print("sudetis +")
print("atimtis -")
print("daugyba ×, *, x, X")
print("dalyba ÷, /, :")
print("pakelti laipsniu **")
print("dalyba be liekanos //")
print("išsaugoti atsakymai: ats")
def calculate():
	num1 = input("num1 ")
	if num1 == "ats":
		for i in range (len(storedats)):
			print("ats nr." + str(i + 1) + " " + str(storedats[i]))
		num1 = storedats[int(float(input("select ")) - 1)]
	else:
		num1 = float(num1)
	simb = (input("simbol "))
	num2 = input("num2 ")
	if num2 == "ats":
		for i in range (len(storedats)):
			print("ats nr." + str(i + 1) + " " + str(storedats[i]))
		num2 = storedats[int(float(input("select ")) - 1)]
	else:
		num2 = float(num2)
	if simb == "+":
		ats = num1 + num2
	elif simb == "-":
		ats = num1 - num2
	elif simb == "×" or simb == "*" or simb == "x" or simb == "X":
		ats = num1 * num2
	elif simb == "÷" or simb == "/" or simb == ":":
		ats = num1 / num2
	elif simb == "**":
		ats = num1 ** num2
	elif simb == "//":
		ats = num1 // num2
	if ats == int(ats):
		ats = int(ats)
	print("atsakymas " + str(ats))
	storedats.append(ats)
	calculate()
calculate()