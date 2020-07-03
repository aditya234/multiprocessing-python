import random

score = 0

running = True
while running:
    randomInt = random.randint(1, 7)
    inputInt = input(f"Enter int {randomInt}\n")
    if str(inputInt) == str(randomInt):
        score += 1
    else:
        print(f"\n\nEnd score is {score}")
        running = False
