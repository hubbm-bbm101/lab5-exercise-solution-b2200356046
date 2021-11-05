import random
number = random.randrange(0, 100)
guess = int(input("Guess a number between 0 and 100 "))
while guess != number:
    if guess > number:
        guess = int(input("Decrease your number! "))
    else:
        guess = int(input("Increase your number! "))
if guess == number:
    print("You guessed the right number! It is " + str(number) + ".")
