hexNum = input("Type an hexadecimal number: ").lower();

def getHexNum(hexChar):
    hexPossibleChars = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
    num = -1
    for x in range (len(hexPossibleChars)):
        if hexPossibleChars[x] == hexChar:
            num = x+1
    return num

def hexCheck(hexNum):
    isHex = True
    for char in hexNum:
        if char.isalnum():
            if getHexNum(char) == -1:
                isHex = False
        else:
            isHex = False
    return isHex

def hex_to_decimal(hexNum):
    num = 0
    div = 16
    
    for x in range (len(hexNum)):
        num += pow(div, (len(hexNum) - (x+1))) * getHexNum(hexNum[x])
    return num

if hexCheck(hexNum):
    print("The equivalent decimal number for hexadecimal \"{}\" is  {}".format(hexNum, hex_to_decimal(hexNum)))