import random
from random import randint


print "Hello! Welcome to our game!:)"
print "What's your name?"
name = raw_input("(type in your name) ")

print "%s, I am thinking of a number between 1 and 100. Try to guess my number." % name
number = int(raw_input("Your guess? "))

computer_choose = randint(1,100)
print computer_choose

count = 1
while number != computer_choose:
    if number < computer_choose:
        print "Your guess is too low, try again."
    elif number > computer_choose:
        print "Your guess is too high, try again."
    number = int(raw_input("Your guess? "))
    count += 1

print "Well done, %s! You found my number in %d tries!" % (name, count)