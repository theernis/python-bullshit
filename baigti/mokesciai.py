suma = 0
minus = 0
def test():
	suma = float(input("uzdirbta "))
	minus = float(input("mokesciams "))
	ats = suma / 100 * minus
	ats = int(ats * 100) / 100
	print("sumokek: " + str(ats))
	test()
test()