print("Introuce el tiempo 1 (h m s): ")
strT1 = input()
arrayT1 = strT1.split()

print("Introuce el tiempo 2: ")
strT2 = input()
arrayT2 = strT2.split()

def CalcSeg(arrayT):
    segundos = (int(arrayT[0])*3600) + (int(arrayT[1])*60) + int(arrayT[2])
    return segundos

t1 = CalcSeg(arrayT1)
t2 = CalcSeg(arrayT2)

tf = t1 - t2

print("La diferencia es de: %d s." %tf)

    

