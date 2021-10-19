cont = 0
max = 10 # times the user can type 'a'

while cont < max:
    c = input("Type a char: ")[0]

    if c == 'a': 
        cont += 1
    
        print("%d 'a' remaining" %(max-cont))

    




