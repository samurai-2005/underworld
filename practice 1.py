import random

# Awroken

MINIMUM = 1
MAXIMUM = 99
NUMBER = random.randint(MINIMUM, MAXIMUM)
GUESS = None
ANOTHER = None
TRY = 0
RUNNING = True

print ("Alright...")

while RUNNING:
    GUESS = input("What is your lucky number? ")
    if int(GUESS) < NUMBER:
        print ("Wrong, too low.")
    elif int(GUESS) > NUMBER:
        print ("Wrong, too high.")
    elif GUESS.lower() == "exit":
        print ("Better luck next time.")
    elif int(GUESS) == NUMBER:
        print(f"Yes, that's the one, {NUMBER}.")
        if TRY < 2:
            print(f"Impressive, only {TRY} tries.")
        elif TRY > 2 and TRY < 10:
            print(f"Pretty good, {TRY} tries.")
        else:
            print(f"Bad, {TRY} tries.")
        RUNNING = False
    TRY += 1