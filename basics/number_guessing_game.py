import random

magic_num = random.randint(1,100)

print("Guess the number between 1 to 100")

playing = True

attempt = 0

while playing:
    num = int(input("Guess the number: "))
    attempt += 1
    if num > magic_num:
        print("It's below", num)
    elif num < magic_num:
        print("It's above", num)
    else:
        print("You guessed in", attempt, "attempts")
        playing = False