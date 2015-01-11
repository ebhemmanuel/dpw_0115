__author__ = 'emmanuelbarreto'                                               # Assuming this displays the author somewhere?

# Emmanuel Barreto
# Jan 10 2015
# Lab 1 Madlib

print " "                                                                    # A simple spacer.

user = raw_input("Your name: ")                                              # A raw input that asks for your name
second_user = raw_input("Your bestfriends name: ")                           # A raw input that asks for your bestfriends name
year = raw_input("What year is it!?(- yelled Robin Williams) : ")            # Choose a random year, play Jumanji. GO
fridge = raw_input("How many times do you open the fridge a day?: ")         # No really, how many times do you do it.
words = ["kicked", "sold", "chopped", "Nope."]                               # My word bank, not really effective but yea.


def plot(s1, s2):                                                            # A function with two arguments
    result = str(s1) + " " + str(s2)                                         # A variable holding both arguments (redundant)
    return result                                                            # returns the result


ending = plot("The", "End")                                                  # variable that actually holds the function and the arguments with it

# Here we'll have an array of 4 items, in this case we'll use
# the array to go through the story with the a loop.

chapter = ['''
When {user} was young, he tried to leave behind his past.
Instead, {second_user} helped {user} understand his life.
Believe it or not, {user} turned his life upside down very quickly... again.
So it was up to {second_user}, to save our world.
The year was {year}, and {second_user} had  already {word}
and killed {fridge} cyborgs. He had become a serial killer.

''', '''
Little did {user} know, that his actions would have a greater effect than he expected.
As soon as he found out, {second_user}, had already been to the ends of the world.
No one could face the wrath of the cyborg serial killer! Often did {user} think
of all the terrible things he had done. He had {word} millions of humans to an
underground organization. He couldn't believe what he was witnessing. His bestfriend,
becoming a terror to humanity, he was so proud...

''', '''
Instead of saving the world, they both ended up becoming the rulers of it.
They had {word} communities apart, and dismembered their governments into disabled providences.

''', "\n{ending}\n"]


# Loops Positive
for i in range(0, 4, 1):                # A for loop that goes from 0 to 4.
    d = {"user": user,                  # My dictionary, holds all the info I need, instead of running local.
         "second_user": second_user,    # Hold the name of bestfriend.
         "year": year,                  # Holds a random year.
         "fridge": fridge,              # holds the amount of times you open your fridge a day!
         "word": words[i],              # Goes through the array of words to replace.
         "ending": ending}              # Runs the ending function.
    print chapter[i].format(**d)        # It's going to print out the chapter number per loop from the array.
    import time                         # Requests current time from module?
    time.sleep(2)                       # Delays next action for 2 seconds.
    if i == 2 or i == 3:                # If i equals 2, then print out "Chachan!"
        print "Chachan!\n"              # Prints out CHACHAN!!
        print "......................................."