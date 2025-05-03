import random
number = random.randint(1, 50)
print("Guess a number between 1 and 50")
guess = int(input())
if guess == number:
    print("You win!")
else:
    print(f"Wrong! The number was {number}")
