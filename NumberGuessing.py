import random
number = random.randint(1, 9)
chance=0
while (chance < 5):
    guess = int(input("Enter the number between 1-9 : "))
    if (guess > number):
        print("Your guess is too high")
    elif (guess == number):
        print("Congratulations! You guessed it correct")
    else :
        print("Your guess is too low")
    chance = chance + 1
if (chance > 5):
    print("No more chances left!, the number is ",number)