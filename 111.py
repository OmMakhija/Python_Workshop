import random

def guess_number():
    return random.randint(1,999)
target_number=guess_number()
attempts=0

while True:
    user_guess=int(input("Guess a number"))
    attempts+=1
    if (user_guess==target_number):
        print("GG lad good guess  no. of attempts="+attempts)
        break
    elif(user_guess<target_number):
        print("Go high or go home")
    else:
        print("You flew too high lad,try going lower")