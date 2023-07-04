# questions

def coffee():
    pi = 3.14
    d = input("What is the diameter? ")
    h = input("What is the height? ")
    v = round(pi * (float(d) * float(d) / 2) * float(h), 2)
    total = "Your total volume is " + str(v)
    return total
print(coffee())


