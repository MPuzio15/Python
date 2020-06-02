import random
#lotto

number = random.randint(1,10)

for i in range(3):
    answer = input("Guess which number from range <1,10) has been drawn \n")
    if number == int(answer):
        print("That's right!")
        break
    else:
        print("Try again:(")
        print()
print("Number chosen by computer was: ", number)








