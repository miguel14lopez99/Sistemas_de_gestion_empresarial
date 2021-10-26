def menu():
    print('-Menu- Choose an option\n',
        '0. Exit  \n',
        '1. $ to €\n',
        '2. € to $\n')

    opt = int(input("Type the option: "))

    while opt < 0 or opt > 2:
        menu()
        opt = input("Error, Type the option: ")
    return opt

def dollar_to_euro():
    dollar = float(input("Type the amount of dollars: "))
    euro = round(dollar * 0.86 ,2)
    print("{}$ are {}€".format(dollar, euro))

def euro_to_dollar():
    euro = float(input("Type the amount of euros: "))
    dollar = round(euro / 0.86 ,2)
    print("{}€ are {}$".format(euro, dollar))

opt = menu()

while opt != 0:
    if opt == 1:
        dollar_to_euro() 
    if opt == 2:
        euro_to_dollar()

    opt = menu()
