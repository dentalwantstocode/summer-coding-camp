print(0 ** 0)
print(13 // 2) # floor division (rounds)
print(29 % 2) # long division remainder
print(3 ** 2) # exponent

# rounding
x = 1.223456789
print(round(x,5)) # the number at the end is how many d.p it will be rounded to

z = 5
y = 6
area = z * y
print(area)

# naming variables
i = 3
I = 4
_i = 5
i1 = 6

# must start with _ or small/large letter, must only contain letters, numbers, and underscores, no dashes stars slashes commas etc...
# age =/= aGe =/= AgE

# etiqquete for naming variables:
# start name with small letter, multiword name -> using camel-case (farisqadan is wrong, do farisQadan)

'''
This is a comment block.
We use this to comment long blocks of code
We also use it to describe code.
'''

# variable types
a = 5 # int (integer)
b = 7.2 # float (decimal)
c = "Yo" # str (string)

name = 'Ali'
surname = 'Gangat'
print(name)
num = '2'
num2 = '5'
print (num + num2) # added the strings together

num = int(num)
num2 = int(num2)
print(num + num2)

print(type(num)) # describes type of variable (int)

ad = 'adam'
ga = 'gangat'
print(ad + ga)

'''
nameeee = "Saeed"
nameeee = int(name)
'''

'''
fl = "5.33333"
print(type(fl))
fl = int(fl)
print(fl)
'''

# cant turn fl into int. but we can turn anything into a string

g = 5
g = str(g)
print(type(g))

# Addition of strings

name1 = 'Adam'
surname2 = 'Gangat'
fullname = name1 + ' ' + surname2

# fullname = hw

# Functions (Average of three numbers)

def average(num5, num6, num7):
    add = num5 + num6 + num7
    avg = add / 3
    return avg
print(average(1, 2, 3))

# Average of four numbers

def average4(num5, num6, num7, num8):
    add = num5 + num6 + num7 + num8
    avg = add / 4
    return avg
print(average(56, 13, 12, 1))

# Find average of friends' ages

def friends():
    friend1 = input("What is your age? ")
    friend2 = input("What is your age? ")
    friend3 = input("What is your age? ")
    add = int(friend1) + int(friend2) + int(friend3)
    avg = add / 3
    avg = round(avg, 3)
    sentence = "The average age is " + str(avg)
    return sentence
print(friends())

'''# conditionals
# if condition:
#   do something
#   print(...)
#   do multiple things

def grades(grade):
    if (grade > 90)
    print("Congrats! You got an A.")
grades(95) # prints the above
grades(60) # does nothing

def gradesComplex(grade):
    if (grade > 90):
        print("Congrats! You got an A.")
    else:
        print("You did not get an A.")
gradesComplex(95)
gradesComplex(60)

def finalGrade(grade):
    if (grade > 90):
        print("You got an A")
    else:
        if: (grade > 80):
             print("You got a B") # and keep going it works .

# but also you can do

def finalGrade(grade):
    if (grade > 90):
        print("You got an A")
    elif (grade > 80):
        print("You got a B")
    elif (grade > 70):
        print("You got a C")
    else:
        print("You failed")
finalGrade(75)

# True / False in Python
95 > 90 ==> True
90 > 95 ==> False
True False
if (True):
    # do something
if (False):
    # do something
0 ==> False
1, 2, 3, ... ==> True
if (1):
    # do something
if (0):
    # this will not execute
"jjjjjj" ==> False
"efiheihjduihdj" ==> True

# Combining conditions
x > 80 and x < 90 # same as 80 < x < 90

if (x > 80 and x < 90)
   # do something

# eg 
x = 85
if (x > 80 and x > 90)
   print("Hello")

if (x > 80 or x < 50)
   print("Bye")
'''

'''

# loops

# print numbers 1-10
print(1) # ......

'''

# while loops

# Basic loop
i = 0
while i < 10:
    print(i)
    i = i + 1
 print("Done.")
# loop()

# Diff b/w loop and conditional
def cond():
    i = 0
    if i < 10:
        print(i)
        i = i + 1
    print("Done.")
# cond()

# name == 'faris' True
# name != 'faris' True

# cond1 and cond2 --> both MUST be true
# cond1 or cond2 --> ONE must be true

# Check for correct password
def passCheck(correctPass):
    password = input("What is your password? ")
    tries = 0
    while password != correctPass and tries < 3:
        tries = tries + 1
        password = input("Try again. ")
    if tries >= 3:
        print("LOCKED OUT ")
    else:
        print("Welcome to the app ")
passCheck("RFS")

# faris != RFS --> True
# mohammad != RFS --> True
# RFS != RFS --> False

# Average of 'n' numbers
def avg():
    num = input("What is your first number? ")
    add = 0
    count = 0
    while num!= "stop":
        add = add + int(num)
        count = count + 1
        num = input("Next number: ")
    avg = add / count
    print("Your avg is " + str(avg))
avg()


# print up to a known number
def numberPrinter(n):
    i = 0
    while i < n:
        print(i)
        i = i + 1
number(5)

# for loop
def forNumberPrinter(n):
    for i in range(n):
        print(i)
forNumberPrinter(10)

# range ()
# ALWAYS stop at 'stop - 1'
# ALWAYS start at start
# range(stop) -> stop after n times
# range(start, stop) -> run stop - start times
# range(start, stop, step)
# DEFAULT START = 0
# DEFAULT STEP = 1

# eg : for i in range(2, 10, 2):
    print(i)

def forLoops():
    print("range(5)")
    for i in range(5):
        print(i)

    print("range(5, 10)")
    for i in range(5, 10):
        print(i)

    print("range(0, 10, 2)")
    for i in range(0, 10, 2):
        print(i)

    print("range(10, 0, -1):)
    for i in range(10, 0, -1):
          print(i)

    print("range(-5):)
    for i in range(-5):
          print(i) # nothing happens
forLoops()

'''
same as the las two lines above the first (2nd last)
         i = 0
          while i > 10:
          print(i)
          i = i - 1
'''

# Small trick for writing i = i (+-*/) 1
# i = i + 1
# i += 1
# i = i - 1
# i -= 1
# i = i * 5
# i *= 5
        
# missed some notes (get them later)

# Advanced string methods

# String indexing
s = "hello"
print(s[0]) # we start counting at 0, not 1
print(s[1])
print(s[4])

# the index we want goes in the square brackets

# the result of this is one single character

# always start count at 0

# always end count at len(s) - 1 (n - 1)

def index(s):
    print("First index: ")
    print(s[0])

    print("Second index: ")
    print(s[1])

    print("Last index: ")
    print(s[len(s) - 1])
    print(s[-1])

    print("Second to last index: ")
    print(s[-2]) # we dont usually use this
index("faris")

s = "hello"
print(s[5]) # doesn't work
print(s[-5]) # doesn't work

# Review of loops from last time
def loop1(s):
    for c in s:
        print(c)
loop1("hello)

# Rewriting loop1() using indeces
def loop2(s):
    for i in range(len(s)):
        print(s[i])
loop2("hello")

# Function that returns a string with every other letter
# ramallah --> rmla
def everyOther(s):
    t = ""
    for i in range(0, len(s), 2):
        t = t + s[i]
    return t
def everyOther1(s):
    t = ""
    for i in range(len(s)):
        if i % 2 == 0: # i % 2 for every 2nd character
            t = t + s[i]
    return t
print(everyOther("ramallah"))
print(everyOther1("ramallah"))
# same results

# slicing
# s = "ramallah"
# t = "allah"
# t = s[3:7]
# generally:
# string[start:stop + 1]
# string[start:stop + 1:step]
# default values:
# start = 0
# end = len(string) - 1
# step = 1

def slicing():
    st = "elephant"

    print(st[2:5]) # prints eph
    print(st[4:100]) # actually prints hant, no error
    print(st[12:16]) # empty nothing
slicing()

# rewritee everyOther() using slicing

    print(st[0:len(st):2])
    print(st[0::2])
    print(st[::2])
slicing()

# all produce the same thing

# rewrite reverse()
print(st[::-1])
slicing()

# some more string methods
def moreStrMethods(s):
    print(s.isdigit()) # is it a number or not
    print(s.isupper()) # is it uppercase or not
    print(s.islower()) # is it lower case or not
moreStrMethods("JoekojiuDHeio") # false for respective case
moreStrMethods("2678920879") # true for respective case
moreStrMethods("2u8yhugbh8h") # false for respective case

def evenMoreMethods(s):
    print(s.lower()) # turns lower
    print(s.upper()) # turns upper
evenMoreMethods("cjhiDOUJHIDJo") # false

def moreMethods(s):
    # removes all whitespace before and after string
    # s = "      ishi          ishue ojheihis  "
    # returns whole string without those spaces
    print(s.strip())
    print(s.strip(","))
    # s = ", faris,"
    # becomes " faris"

    # find: find first instance of input
    # if the string doesn't have the input, -1
    print(s.find("h"))

# find second instance of character in string
# elephant, we want e
# we should get 2, not 0

def secondFind(character, string):
    firstInstance = string.find(character)
    # use slicing to reduce the string called elephant
    slice = string[firstInstance + 1:]
    secondInstance = slice.find(character) # 1
    return firstInstance + secondInstance + 1
print(secondFind("e", "elephant"))
    # elephant
    # first instance of e = 0
    # lephant
    # returns 2

# Conditionals
# if my favorite subject is Biology
# then I should take Biology in IB
# otherwise, I should take Chemistry

#if condition:
    # do something
    # can do multiple things

'''
x = 20
if (x > 25):
    print("x is above 15")
'''

def gradeCalc(grade):
    if (grade > 90):
        print("Congrats! You passed!")
    else:
        print("Better luck next time")
gradeCalc(65) # Better luck next time
gradeCalc(95) # Congrats!


def grades(grade):
    if (grade > 90):
        print("You got an A")
    elif (grade > 80):
        print("You got a B")
    elif (grade > 70):
        print("You got a C")
    else:
        print("You got an F")
grades(50)
grades(90)

'''
# True / False: different representations
90 > 70 : True
60 > 70 : False
70 > 70 : False
70 >= 70: True

name == "Faris" # is equal to
name != "Faris" # not equal to

True # this is true, run the condition
False # this is false, do not do the condition

if (True):
    print("Hi")

if (0):# 0 evaluates as False
if False: # False evaluates as False
if 70 > 90: # 70 > 90 is False

'''







def foodDelivery(tax_percentage, food_cost, distance):
    tax_percentage = int(tax_percentage)
    tax = (tax_percentage / 100) * food_cost
    tip = (tax + food_cost) * 0.2
    deliveryFee = 5 + distance
    totalCost = round((tax + food_cost + tip + deliveryFee), 2)
    print("Your total is " + str(totalCost) + " NIS. Delivery is expensive.")
foodDelivery(10, 20, 40)
foodDelivery(5, 2, 25)



def minCoins():
    tens = int(input("How many 10 NIS do you have? "))
    five = int(input("How many 5 NIS do you have? "))
    twos = int(input("How many 2 NIS do you have? "))
    ones = int(input("How many 1 NIS do you have? "))
    total = float((tens * 10) + (five * 5) + (twos * 2) + (ones * 1))
    tens_cnt = total // 10 # eg: 37 // 10 = 3
    five_cnt = (total - (tens_cnt * 10)) // 5
    twos_cnt = (total - ((tens_cnt * 10) + (five_cnt * 5))) // 2
    ones_cnt = (total - ((twos_cnt * 2) + (tens_cnt * 10) + (five_cnt * 5))) // 1
    print(tens_cnt, ", ", five_cnt, ", ", twos_cnt, ", ", ones_cnt)
minCoins()

# Loops
'''
i = 0
while i < 10:
    print(i)
    i = i + 1
'''

# While loops
def loop():
    i = 0
    while i < 10:
        print(i)
        i = i + 1
    print("Done!")
# loop()

def cond():
    i = 0
    if i < 10:
        print(i)
        i = i + 1
    print("Done!")
# cond()

# name == "Faris"
# name != "Faris"
# cond1 and cond2 -> both MUST be true
# cond1 or cond2 -> ONE must be true

# Password checker
def passwordCheck(correctPass):
    pw = input("What is your password? ")
    numOfTries = 0
    while pw != correctPass and numOfTries < 3:
        numOfTries = numOfTries + 1
        pw = input("Wrong! Try again. ")
    if numOfTries >= 3:
        print("LOCKED OUT OF ACCOUNT.")
    else:
        print("Welcome to the app.")
# passwordCheck("RFS")


# Find average of 'n' numbers
def avg():
    text = input("What is your first number? ")
    sum1 = 0
    count = 0
    while text != "stop":
        if text != "stop":
            text = int(text)
            sum1 = sum1 + text
            count = count + 1
        text = input("Next number? ")
    avg = sum1 / count
    print("Average is " + str(avg))
#avg()


# Print "Hello" 3 times
def three():
    count = 0
    while count < 3:
        print("Hello")
        count = count + 1
# three()

def nTimes(n):
    count = 0
    while count < n:
        print("Hello")
        count = count + 1
# nTimes(10000000) # do not do this!


# For loops
def listing(n):
    '''
    i = 0
    while i < n:
        print(i + 1)
        i = i + 1
    '''
    for i in range(n):
        print(i)
# listing(10)

# range() function
# range(stop)
# range(start, stop)
# range(start, stop, step)

def forLoops():
    print("range(5)")
    for i in range(5):
        print(i)

    print("range(1, 10)")
    for i in range(1, 10):
        print(i)

    print("range(1, 10, 2)")
    for i in range(1, 10, 2):
        print(i)

    print("range(10, 1, -1)")
    for i in range(10, 1, -1):
        print(i)
# forLoops()

def enough_sleep(classes_taken, school_clubs, down_time, test_next_day):
    classes_taken = classes_taken * 2.5
    school_clubs = school_clubs * 0.5
    test_hours = 0
    if test_next_day == True:
        test_hours = 5
    else:
        test_hours = 0
    total_time = 24 - (school_clubs + classes_taken + down_time + test_hours)
    if total_time <= 6:
        return("I'm tired!")
    elif total_time > 6 and total_time < 8:
        return("That's alright.")
    else:
        return("Thank goodness...")

def birthday_party(num_attendees, avg_age):
    num_attendees = int(num_attendees)
    avg_age = int(avg_age)
    if num_attendees <= 15:
        return("Venue: Home")
    elif num_attendees <= 30:
        return("Venue: Arcade")
    else:
        if avg_age <= 14:
            return("Venue: Amusement Park ; Type of Ride: Kid Rides")
        else:
            return("Venue: Amusement Park ; Type of Ride: Regular Rides")
# Loops and Strings

def loop():
    # For loop
    for i in range(5):
        print(i)
    # While loop 
    i = 0
    while i < 5:
        print(i)
        i += 1 # == i = i + 1

# s = "word"
# print(s)
# s = int(s)

def strLoop(s):
    # s here is a string parameter
    # print every character in 's'
    # eg: s = "hello"
    # ==> h, e, l, l, o
    for character in s:
        print(character)
# 'character' can be any variable name
# typically: character, char, c, i, faris
# iterates through the string letter by letter
# strLoop("hello")


def strLength(s):
    length = 0
    for char in s:
        length = length + 1
    return length
# print(strLength("hello"))
# print(strLength("oiygidhgiurhiuwhqweihiuh"))

# len(string)
# Built-in, like round(), or print()
# print(len("hello"))


# Count number of vowels in str
def vowels(string):
    # vowels: A, a, E, e, ..., U, u
    vow = 0
    for letter in string:
        if letter in "AaEeIiOoUu":
            print(letter)
            vow = vow + 1
    return vow
# print(vowels("elephant"))
# print(vowels("ElepHAnt"))

# Return True if all character in 0-9
# Return False if any character not 0-9
def isDigit(s):
    result = True
    for letter in s:
        if letter not in "0123456789":
            result = False
            break
    if s == "":
        result = False
    return result
'''
print(isDigit("023872874")) #True
print(isDigit("379872k23472358972598897287")) #False
print(isDigit("")) #False
print(isDigit("_")) #False
'''

# More on loops
def loop1():
    # For loop
    for i in range(5):
        print(i)
    # While loop 
    i = 0
    while i < 5:
        print(i)
        i += 1 # == i = i + 1

# break: if the program hits this statement,
# it immediately quits the loop and
# moves to the next code after the loop

# continue: skip the next iteration of the loop
# example: on i = 5, skip 5, and move to i = 6

# pass: do nothing, not used very often

# Using break, continue, pass
def example():
    word = "go team"
    for letter in word:
        if letter in "ae":
            break
        if letter in "gt":
            continue
        if letter in " ":
            pass
        print(letter)
    print("Done")
# example()

# Create copy of a string
def strcpy(s):
    t = ""
    for char in s:
        t = t + char
        print(char)
        print(t)
    return t

# s = "Ramallah Friends School"
# We want to remove spaces from s
# RamallahFriendsSchool
# s[8] = "" does NOT work

# Function to remove spaces from string
def despace(s):
    t = ""
    for char in s:
        if char not in " ":
            t = t + char
    return t
# print(despace("Ramallah Friends School"))


# Function to reverse a string
# faris -> siraf
def reverse(s):
    t = ""
    for i in range(len(s) - 1, -1, -1):
        t = t + s[i]
    return t
print(reverse("hello"))

# Another more creative way to reverse a string
def reverse1(s):
    t = ""
    for char in s:
        t = char + t
        # usually, we do t = t + char
    return t
print(reverse1("faris"))


# s = cat
# return cattac
# s = faris
# return farissiraf
def mirror(s):
    s = reverse(s) # used the function we wrote
    t = ""
    for char in s:
        t = char + t + char
    return t
print(mirror("hello"))

# String indexing
# s = "hello"
# s[1]

# Every character in a string has an index number
# Start: 0
# End: len(string) - 1
# s = "hello"
# First index (0): 'h' --> s[0]
# Last index (4): 'o' --> s[4]
# s[5] --> gives an error, as length is 5
'''
s = "hello"
print(s[0])
print(s[2])
print(s[4])

s = "dfgiuhfiuhasefihweiufhqriwhiquewrh"
print(s[-1])
print(s[len(s) - 1]) # don't really do this

def index(s):
    print("The first character of s is: ")
    print(s[0])

    print("The second character is:" )
    print(s[1])

    print("The last character is: ")
    print(s[-1])

    # print("This does not work: ")
    # print(s[50])
    # gives string index out of range
index("hello")

s = "Hello"
print(s[-2])
print(s[-3])
print(s[-5])
# From the negatives, only -1 is frequently used


# Review of loops for strings
def loop1(s):
    for char in s:
        print(char)
loop1("freddie")

def loop2(s):
    for i in range(len(s)):
        print(i, s[i])
loop2("freddie")
        
# More advanced string functions

# Function to return a string with every other letter
## faris --> frs
def everyOther(s):
    t = ""
    for i in range(0):
        # check if number is even
        if i % 2:
            t = t + s[i]

    #for i in range(0, len(s), 2):
     #   t = t + s[i]

    return t
print("Here")
print(everyOther("faris"))


# Slicing
s = "ramallah friends school"
print(s[9:16])

# Slicing rules
# used to extract specific range of indeces
# string[start : stop + 1]
# string[start : stop + 1 : step]
# string[0:-1:2]
# string[0::2]
# Default values:
# start = 0
# end = len(s) - 1
# step = 1

# Examples of slicing
def slicing():
    s = "elephant"
    print(s[2:5])
    print(s[4:108968960])
    print(s[12:16])
    # Recreate the everyOther() function
    print(s[0:-1:2])
    print(s[0::2])
    print(s[::2])
    # All 3 of the above do the same thing
    print(s[::-1])
slicing()


# Final built-in string methods
def stringMethods(s):
    print(s.isdigit())
    print(s.isupper()) # checks if string is upper case
    print(s.islower())
stringMethods("sdfnsndfn")
stringMethods("2539723489")
'''

def moreMethods(s):
    print(s.upper()) # turn to upper case
    print(s.lower()) # turn to lower case
moreMethods("uhUbIYsiudgIUghefbu")


def evenMoreMethods(s):
    # removes all leading and trailing whitespace
    # eg: s = "   iwefihjw  hnlsknd   "
    # becomes "iwefihjw  hnlsknd"
    print(s.strip())
    # if input given, remove starting and ending instances
    # of input
    # s = ", faris,"
    # becomes " faris"
    print(s.strip(","))

    # find
    # gives index of first instance
    # of input
    # if input is not in string
    # returns -1
    print(s.find("h"))
    if "h" in s:
        print(s.index("h"))
    else:
        print(-1)

# Find second occurance of a character in a string
# s = "hellohello"
# string.find("h")
# firstInstance = 0
# ellohello
# "ellohello".find(h)
def secondFind(string, char):
    firstInstance = string.find(char)
    slice = string[firstInstance + 1:]
    secondInstance = slice.find(char)
    print(firstInstance + secondInstance + 1)
secondFind("elephant", "e")

### Lists ###
# Similar to str, int, this is a data type

# To make a list, use [] and seperate components w/ commas (,)
# Very similar operations to strs
def lists1():
    myList1 = ["red", "blue", "green"]
    myList2 = [1, 4, 6]
    print(myList1)
    print(myList2)
    print(type(myList1))
    myList3 = ["red", 5, 7.8]
    print(type(myList3))
    print(myList3[1])
    print(type(myList3[1]))
    print(len(myList3))   
# lists1()

# Strings are not mutable
# Lists ARE
def lists2():
    myList = ["apples", 7, "fred"]
    print(myList)
    # Change lists at position 1
    myList[1] = 2.8
    print(myList)

    # We cannot do this:
    # myStr = "Hello"
    # myStr[1] = "f"
    # This gives an error
# lists2()

def addList():
    fruits = ["apples", "oranges"]
    print(fruits, len(fruits))

    # Add bananas to the list
    # This does not work
    # fruits = fruits + "bananas"

    fruits.append("bananas")
    # To add to end of list, use list.append(...)

    fruits = fruits + ["straberries"]
    # We can only add things of the same type
    print(fruits)
# addList()


def lists3():
    myStr = ""
    myList = [] # empty list
    print(myList, len(myList))
    myList.append("Faris")
    print(myList, len(myList))
# lists3()

# Removing items from list
def lists4():
    myList = ["apples", "oranges", "bananas", "tomatoes"]
    print(myList, len(myList))
    del(myList[-1])
    print(myList, len(myList))
# lists4()

# Lists are VERY similar to strings
# .append()
# del(index)
# max(), min()
# .index()
# sort()
# slicing
# We will see these after the break


def listSlice():
    myStr = "Hello World"
    print(myStr[1:4]) # ell

    myList = ["apples", "oranges", "bananas", 1, 3, 5]
    print(myList[1:5])
    print(myList[1:100])
    print(myList[30:50])
    list2 = []
    print(myList[0:5])

    # Slicing to reverse a list
    print(myList[::-1])
# listSlice()


# We can also make lists of lists
def listOfLists():
    myList = [["h", "i", "j"], 6, "hello"]
    print(len(myList))
    print(type(myList))
    print(type(myList[0]))
    newList = myList[0] # ["h", "i", "j"]
    print(newList[1])
    print(myList[0][1])
listOfLists()

def loopOnStrings():
    myList = [["a", "b", "c"], [1, 2, 3, 4]]
    for item in myList:
        for char in item:
            print(char)
loopOnStrings()

# This is what we call a nested loop


def harderLoop():
    myList = [[1, 2, 3], 5, "hi", ["hello", "world"]]
    for item in myList:
        if type(item) != list:
            print(item)
        else:
            for char in item:
                print(char)
harderLoop()

### Tuples ###

# List: [1, 2, "hello"]

# Tuples are similar to lists
# but enclosed in () instead of []
# tuples usually used in databases
# want to associate 3 pieces of info with a student
# we could change elements in a list
# student = ["mohd.", 15, "physics"]
# student[1]="hello"

def tuples1():
    person = ("Faris", 22, "student")
    print(person)
    print(type(person))

    print(person[1])
    # index can never be out of range
    # we can use -1 for last value

    # we can also do slicing
    slice = person[1:4]
    print(slice)

    # we can have an empty tuple
    # this is denoted by ()
    print(())

    # here, we start to get different to lists...
    myList = [3]
    print(type(myList))

    myTuple = ("Hello")
    print(myTuple, type(myTuple))

    # how can we put a single item in a tuple?
    a = ("Hello",)
    print(a, type(a))
    print(len(a))

    # another difference between the two
    myList = ["apple", 5, "oranges"]
    myList[1] = "bananas"
    print(myList)

    myTuple = ("apple", 5, "oranges")
    myTuple[1] = "bananas"
    print(myTuple)  
# tuples1()


def tuples2():
    # packing a tuple
    x = ("Faris", "student", 22)

    # unpacking a tuple (made easy)
    (name, job, age) = x

    # we can now use these as three different vars
    print(name, type(name))
    print(job, type(job))
    print(age, type(age))

    # difference with lists:
    y = ["Faris", "student", 22]
    # to 'unpack' a list is pretty hard
    name = y[0]
    job = y[1]
    age = y[2]
    print(name, type(name))
    print(job, type(job))
    print(age, type(age))
# tuples2()


def swapping():
    a = 4
    b = 5

    # we want to swap the values, so that:
    # a = 5 and b = 4

    (a, b) = (b, a)
    print(a)
    print(b)
# swapping()

# takes in radius and returns circumf. and area
def circle(r):
    # reminder: ^ does XOR
    # ** does to the power
    area = 3.1415 * (r ** 2)
    circ = 3.1415 * (r * 2)
    return (round(area, 2), round(circ, 2))
# print(circle(5))

# tuples for databases
# function to make grocery database
def groceryList():
    # user inputs item name, price, quantity
    # type stop when done adding
    # build a list of tuples and return the list\
    gList = []
    item = ""
    while item not in ["stop", "enough"]:
        item = input("What is your item name? ")
        if item == "stop":
            break
        price = float(input("Item price? "))
        quant = int(input("How many? "))
        # pack in a tuple...
        entry = (item, price, quant)
        gList.append(entry)
    return gList
print(groceryList())
        
# now, let's buy all our groceries
def buyGroceries(gList):
    cost = 0.0
    for item in gList:
        # unpack items
        (name, price, qty) = item
        print(name + ":" + str(qty) + ", " str(price))
        cost = cost + price * qty
    print("Total cost: " + str(cost))

### Dictionaries ###

# Reminder:
# lists -> [5, "hello", [1, 2, 3]]
# tuples -> (5, "hi") or (6,)
# Can we use {} for lists or tuples?

# Dictionaries are similar to lists
# They use {}, not [] nor ()
# We store key, value pairs
# dict = {"hello":"word for greeting"}

# the keys in a dict can be strings or any data type
# but keys must be unique
# lists: [5, 5, 5]
# dict: {5:"hi", 5:"hello"} not allowed
# values can be anything, no need to be unique

def dict1():
    # dict of keys: letters, values: numbers
    myDict = {"a":1, "b":2, "c":3, 1:50}
    print(type(myDict))
    print(len(myDict)) # we have 3 PAIRS
    # indexing in lists and tuples:
    # listOrTuple[index]
    # dict[index] defeats the purpose of using a dictionary
    print(myDict["b"])
    print(myDict[1])
    # we are not indexing
    # we are looking up
    # when we use [], we are getting the VALUE
    # of the KEY we look up
# dict1()


# Function to count number of vowels in a string
def countVowels(string):
    count = {"a":0, "e":0, "i":0, "o":0, "u":0}
    # 5 keys, one for each vowel
    # all starting with unknown quantity (0)
    for c in string:
        if c == "a":
            count["a"] = count["a"] + 1
        elif c == "e":
            count["e"] = count["e"] + 1
        elif c == "i":
            count["i"] = count["i"] + 1
        elif c == "o":
            count["o"] = count["o"] + 1
        elif c == "u":
            count["u"] = count["u"] + 1
    print(count)
# countVowels("qwiofbcqnnewirouvnqwewiqoeufbsb")
            
# Function to look up student grades
namesAndGrades = [("faris", 50), ("mohammad", 90), ("ahmad", 75)]
def lookUpGrades(student):
    for tups in namesAndGrades:
        if tups[0] == student:
            print(tups[1])
            break
# lookUpGrades("ahmad")

gradesDict = {"faris":50, "mohammad":90, "ahmad":75}
def betterLookup(student):
    print(gradesDict[student])
# betterLookup("ahmad")


def dicts2():
    print(gradesDict)
    print(list(gradesDict.keys()))
    print(list(gradesDict.values()))
    sum = 0
    for grade in gradesDict.values():
        sum += grade
    print(sum / len(gradesDict))
#dicts2()

def modifyDict():
    # to add a new key:value pair to your dictionary:
    gradesDict["basil"] = 100
    print(gradesDict)

    # if key already exists, override data already there
    gradesDict["faris"] = 0
    print(gradesDict)

    # to delete a key:value pair:
    del(gradesDict["faris"])
    print(gradesDict)

    # you should always check before deleting:
    if "yousef" in gradesDict:
        del(gradesDict["yousef"])
    else:
        print("Yousef not in this dictionary")
# modifyDict()

def delete(name):
    if name in gradesDict:
        del(name)
    else:
        print("Name not in dictionary")

# Letter frequency
# for example, "dad" to give us {"d":2, "a":1}
def freq(word):
    letters = {} # empty dictionary
    for char in word:
        if char not in letters:
            letters[char] = 1
        else:
            letters[char] += 1
    return letters
print(freq("earioubnsdkjvbsdkjvbsdjaf"))

def used_letter(essay):
    characters = ""
    for item in essay:
        for char in item:
            if char not in characters:
                characters += char
    return (len(characters), characters)

def checkbook(list_of_expenses):
    itemsDict = {} # key:value pairs will be item:totalPrice
    total = 0
    for tups in list_of_expenses:
        # input list: [(itemName, price), (itemName, price)]
        itemName = tups[0].lower()
        total += tups[1]
        if itemName in itemsDict:
            itemsDict[itemName] += tups[1]
        else:
            itemsDict[itemName] = tups[1]
    # make a list of tuples to return
    # .items() gives a tuple of (key, value)
    # item[0] -> item name
    # item[1] -> item price
    finalList = list(itemsDict.items())
    finalList.append(("total", total))
    return finalList

def animal_counter(animals):
    aDict = {}
    for a in animals:
        tempAnimal = a[0].upper() + a[1:].lower()
        if not tempAnimal in aDict:
            aDict[tempAnimal] = 1
        else:
            aDict[tempAnimal] += 1
    return aDict

### Exceptions and Exception Handling ###
def divide(a, b):
    print(a / b)
'''
divide(10, 2)
divide(0, 10)
divide(10, 0)
'''

# We will use exception handling here
def divide2(a, b):
    try:
        # best case is this works
        print(a / b)
    except:
        # but in the worst case, we will do this except block
        print("You cannot divide by zero.")
    # after these, we can continue writing any code we want
'''
divide2(10, 2)
divide2(10, 0)
'''

def divide3(a, b):
    try:
        print(a / b)
    except:
        print("You cannot divide by zero.")
    finally:
        # optional: but will run regardless of try/except 
        print("Done trying this division.")

# myList = [1, 2, 3]
# print(myList[5]) -> this gives us an error (index out of bounds)
def error1():
    myStr = "Hello"
    try:
        print(myStr[10])
    except:
        print("Index out of bounds, try another index.")
    print("Do more things after try/except.")

# Input checking
def error2():
    try:
        x = input("Type a number: ")
        y = int(x)
        print(y * 2)
    except:
        print("User input must be a number.")






### Files and I/O ###

# This is different to what we have done so far,
# since changes stay after the program is complete.
# File lifetime is longer than that of the program.


# Reading a file #
# open(filename, mode)
# filename -> string, with full filename, including extension (.txt, .csv)
# mode -> "w": write; "a": append; "r": read
# file.close()


# Opens a file called filename
# Filename is a str
def readFile(filename):
    file = open(filename, "r")
    # print(type(file))
    text = file.read()
    print(text)
    file.close()
# readFile("poem.txt")

# Function to split our text into a list, by line
'''
Line1
Line2
Line3
'''
# Output: [Line1, Line2, Line3]
def readFileList1(fname):
    myFile = open(fname, "r")
    text = myFile.read()
    myFile.close()
    textList = text.split("\n") # \n = new line character (enter/return)
    print(textList)
readFileList1("poem.txt")


# Using the built-in method to do this
def readFileList2(fname):
    aFile = open(fname, "r")
    myList = aFile.readlines()
    aFile.close()
    print(myList)
#readFileList2("poem.txt")


# checking if file exists or not
def readFile(fname):
    try:
        f = open(fname, "r")
        line = f.readline()
        f.close()
    except:
        print("File " + fname + " does not exist.")
        return
    print(line, end="")
readFile("po1em.txt")


# writing to files
def writeFile(fname):
    try:
        f = open(fname, "w")
        f.write("This is line 1.\n")
        f.write("This is line 2.\n")
        f.close()
    except:
        print("Sorry - file write failed.")
#writeFile("newPoem.txt")

def appendFile(fname):
    try:
        f = open(fname, "a") # append: write at the end of the file
        f.write("This is line 3.\n")
        f.close()
    except:
        print("File does not exist")
appendFile("newPoem.txt")

### CSV Files ###

# CSV: Comma Seperated Value (file.csv)
# header, header, header
# data, data, data
# data, data, data

# time (s), mass (g), speed (m/s)
# 50, 60, 1000
# 123, 1231, 123114

def csvRead(fname):
    '''
    try:
        file = open(fname, "r")
    except:
        print("File does not exist")
    '''
    file = open(fname, "r") # r indicates reading, not writing

    # read and print the header line
    # which describes the data below
    # time(s), mass(g), speed(m/s)
    header = file.readline() # a string
    # removes any leading/trailing whitespace
    header = header.strip()
    header = header.split(",")
    print(header)

    # how many variables are in my data?
    # print(len(header))

    # list to hold our data
    # this will be a list of lists
    # each list will be data for each header
    data = []

    # all row data now in 'rows'
    rows = file.readlines()

    # at this point, we are done with our file
    # we HAVE TO close it
    file.close()

    # print(rows)

    for row in rows:
        # 'row' represents a string
        # which represents one line in city_crime.csv
        line = row.strip().split(",")
        # whitespace includes '\n'

        # we now have a list of our data point
        # [year, ranking, city, rate]
        data.append(line)
    print(data)
# csvRead("city_crime.csv")

    






### Modules ###
# Module is some code someone else wrote
# which performs functionality we may need
# import nameOfModule

# this is also a way to organize your code
# they are still Python files

# there are some modules that come with Python download
# math, random, os, time, string, sys


# let's start with math
'''
in the math module:
def division(a, b):
    fff
    ifjwsifjeij
def mult(a, b):
    iegirgier

-
-
-
import math
math.mult(a, b)
'''

import math

def mathDemo():
    print(round(math.pi, 5)) # pi up to ~10 d.p.
    print(type(math.pi))

    # to find square root:
    print(math.sqrt(25.0))
# mathDemo()

# let's say we only need math.sqrt
# we can import only math.sqrt:
from math import sqrt
# we can now use sqrt() function from math


# we can give our modules nicknames
import math as m
# instead of math.pi, we would use m.pi, etc.
# more useful for something like:
# import ufhsiunsaiuvnsa as u



# Random...
import random

def randomDemo():
    print(random.randrange(3, 9))
    print("Roll the dice...") # 1-6
    print(random.randrange(1, 7)) # [1, 7)

    # random decimal number
    print(random.random()) # 0 -> 0.999999....
# randomDemo()



import time
# this allows us to use physical time in our programs
def timeDemo():
    start = time.process_time()
    # how long has my program been running?

    for i in range(1000000000):
        pass
    stop = time.process_time()
    print(stop - start)
#timeDemo()

import myModule as my
def myModuleTest():
    print(my.dozen)
    print(my.greeting())
    print()
    print(my.square(13))
myModuleTest()

def plantFinder(old_file, new_file, plant_size):
    file = open(old_file, "r")
    lines = file.readlines() # list of everything: ["name\n", ..., "\n", ...]
    file.close()
    cleanLines = [] # big list of plant lists
    temp = [] # for each individual plant
    for line in lines:
        if line == "\n":
            cleanLines.append(temp) # temp: [name, lifespan, size, price]
            temp = [] # clear 'temp' list for the next plant to use
        else:
            temp.append(line.strip()) # otherwise, remove \n from every comp.
    newFile = open(new_file, "w")
    plantsDict = {}
    for line in cleanLines:
        if line[2] == plant_size:
            plantsDict[line[0]] = float(line[1])
            for n in line:
                newFile.write(n + "\n") # 'enter' after we just inputed info
            newFile.write("\n") # 'enter' after each plant we write
    newFile.close()
    return plantsDict

print(plantFinder("plants.txt", "small_plants.txt", "Small"))    
print(plantFinder("plants.txt", "medium_plants.txt", "Medium"))
print(plantFinder("plants.txt", "large_plants.txt", "Large"))

def plantSplitter(new_file, num_people, tax):
    file = open(new_file, "r")
    lines = file.readlines()
    file.close()
    total = 0
    for i in range(3, len(lines), 5):
        total += float(lines[i][1:].strip())
    total += (tax * total)
    return round(total / num_people, 2)
print(plantSplitter("large_plants.txt", 7, 0.6))

