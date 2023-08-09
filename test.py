# input returns name of plant, expected lifetime, plant size, price
def plant_finder(old_file, new_file, plant_size):
    file = open("plants.txt", "r")
    text = file.read()
    file.close()
    textList = text.split('\n')
    location = 0
    f = open("New.txt", "w")
    answer = input("which size do you want?")
    for i in textList:
        if i == answer:
            location = textList.index(i)
            for m in range(location-2,location+3):
                f.write(textList[m] + "\n")
            textList[location] = "temp"
    f.close()


def tax():
    file = open("New.txt", "r")
    text = file.read()
    file.close()
    textList = text.split("\n")
    numP = 4
    tax = 1.2
    total = 0
    for i in textList:
        if i != "":
            if i[0] == "$":
                total = total + float(i[1::])
    total= total*tax/numP
    print(total)
tax()
    
