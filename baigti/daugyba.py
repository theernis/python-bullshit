def count(test):
	test = int(test)
	for y in range(test):
		for x in range(test):
			print(str(y+1)+"×"+str(x+1)+"="+str((y+1)*(x+1)))
		print()
	count(float(input("skaicius:")))
count(float(input("skaicius: ")))