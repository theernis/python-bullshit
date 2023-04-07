def test(metai):
	if metai >= 0:
		liko = metai - metai // 4 * 4
		liko2 = 4 - liko
		if metai - metai // 4 * 4 == 0:
			print("olimpiniai")
		else:
			print("ne olimpiniai")
	else:
		print("ne olimpiniai")
		liko2 = 0 - metai
	print("iki olimpiniu liko")
	print(liko2)
	test(float(input("irasykite metus ")) - 1896)
test(float(input("irasykite metus ")) - 1896)