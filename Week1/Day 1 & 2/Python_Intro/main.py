# -----------------------------------------------------------------------------------------------------

# Emmanuel Barreto
# Jul 8 14
# Intro Python

print " "

# -----------------------------------------------------------------------------------------------------
# Basics

# Grades
def grades(n):
    if n >= 90:
        print "Your grade is A."
    elif n >= 80:
        print "Your grade is B."
    elif n >= 70:
        print "Your grade is C."
    else:
        print "Your grade is F."

grades(69)

# first_name = "Emmanuel"                                 # First Name value
# last_name = "Barreto"                                   # Last Name value
# full_name = first_name + " " + last_name                # Full Name being Displayed

# year_born = 1989                                        # Your year of Birth
# age = 2014 - year_born                                  # The loose way to calculate your age

# # str(age) + " years old."     # Prints out the age of the specific person.
# age = raw_input("Type your age: ")                      # Asks for the age.
# print full_name + " is " + str(age) + " years old."          # Prints out the age of the specific person.

# # -----------------------------------------------------------------------------------------------------

# # Conditionals

# budget = 200
# shoe_price = 60
# won_lottery = True

# if shoe_price <= budget or won_lottery:                 # and / or for && / ||
#     print "Buy da shoes."
# else:                                                   # elif is else if
#     print "no shoes for you!"
#     print "What are you waiting for go!!"

# # -----------------------------------------------------------------------------------------------------

# # Functions
# def calc_area(w, h):
#     pass # empty function?
#     a = w * h
#     return a

# area = calc_area(50, 60)
# print str(area) + " boom"

# # -----------------------------------------------------------------------------------------------------


# Loops Positive
r = range(1,11)                                           # Count from 1, count to 11, counts up by one by default.
# print r
# for i in range(0, 6, 2):                                # Start from 0, count to 6, counts up by twos.
#     print str(i) + "\n"
stuff = range(1,11)
total = 0
for i in stuff:
    total+= i
print total

# for i in range(0, len(r)):                              # len() just return the length of something
#     result = r[i] + r[i]
# print result

# # Loops Negative
# for e in range(6, 0, -1):
#     print str(e) + "\n"

# # -----------------------------------------------------------------------------------------------------

# # Array is a List in Python
# students = ["Yo", "Hey", "No"]                          # My array
# students.append("Maybe")                                # Appends Maybe to the array
# students.pop(2)                                         # Removes en element of an array out of a specific index
# del students[1:3]                                       # Splicing from 1 and 2.
#  for s in students:                                     # Goes through the array
#    print s                                              # Prints out the array

# # -----------------------------------------------------------------------------------------------------

# # While Loop
# i = 0
# while i<5:
#     print i
#     i +=1

# # -----------------------------------------------------------------------------------------------------

# # Objects are Dictionaries in Python
# user_name = "Carmine"

# big_string = '''

# Welcome {user_name}, get ready to be destroyed by this Python Class.
# What you know as earth, will become your living hell.

# '''

# print big_string.format(**locals())                      # If this is not scoped, it will not understand it

# # -----------------------------------------------------------------------------------------------------

# # Obj printing with array
# obj = {"name":["Jordan","Julian"], "age":20, "occupation":"student"}
# print obj ["name"][1]

# # Obj printing
# obj = {"name":"Jordan", "age":20, "occupation":"student"}
# print obj ["name"]


