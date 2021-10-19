strT1 = input("Type the first time (h m s): ")
arrayT1 = strT1.split()

print("Type the second time (h m s): ")
strT2 = input()
arrayT2 = strT2.split()

def CalcSeg(arrayT):
    segundos = (int(arrayT[0])*3600) + (int(arrayT[1])*60) + int(arrayT[2])
    return segundos

t1 = CalcSeg(arrayT1)
t2 = CalcSeg(arrayT2)

tf = t1 - t2

print("The difference is: %d s." %tf)

    

