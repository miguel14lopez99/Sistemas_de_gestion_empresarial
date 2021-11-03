strT1 = input("Type the first time (h m s): ") # take the first time
arrayT1 = strT1.split() # then split the string to get an array with hours, minutes and seconds

strT2 = input("Type the second time (h m s): ") # take the second time
arrayT2 = strT2.split()

def CalcSeg(arrayT): # calculate the seconds of each time
    segundos = (int(arrayT[0])*3600) + (int(arrayT[1])*60) + int(arrayT[2])
    return segundos

t1 = CalcSeg(arrayT1)
t2 = CalcSeg(arrayT2)

tf = t1 - t2 

print("The difference is: %d s." %tf)

    

