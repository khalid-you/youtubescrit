import random
highest = 1000
answer = random.randint(1, highest)
print(answer)   # TODO: Remove after testing
print("Please guess a number between 1 and {}: ".format(highest))
guess = 0
guesses = 1
while guess != answer:
    guess = int(input())
    if guess == answer:
        print("Well done, you guessed it")
        print("You got it in {} guesses".format(guesses))
    else:
        if guess > answer:
            print("Please guess lower")
        else:
            print("Please guess higher")
    guesses += 1
