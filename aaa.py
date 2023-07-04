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

    

