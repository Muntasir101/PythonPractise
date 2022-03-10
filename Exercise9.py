import random

count = 0
user_guess = int(input("Guess The Number: "))
random_number = random.randint(1, 2)

if user_guess < random_number:
    print("Too Low")
elif user_guess > random_number:
    print("Too High")
elif user_guess == random_number:
    print("Exactly Right")
    counts = count+1
    print("Matched", +counts)



