start = float(input("pradinė suma: "))
proc = float(input("procentai: "))
stop = float(input("galutinė suma: "))
def test(t1, t2, t3):
 if(t1<t3):
  print(int(100*(t1+t1/100*t2))/100)
  test(int(100*(t1+t1/100*t2))/100, t2, t3)
test(start, proc, stop)
