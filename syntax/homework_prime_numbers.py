import math

'''
Napisać program, który zapyta o liczbę z zakresu 1-100 
i napisze czy podana liczba jest liczbą pierwszą. 
'''
print("This program checks, if the number provided by you is a prime number. \n "
      "Provide a number in range from  1 to 100: ")
number = int(input())
if(number==2):
    print("2 is a prime number")
elif(number%2 ==0 or number <=1 or number % (math.sqrt(number)) == 0):
    print(number, " is not a prime number. ")
else:
    print(number, " is a prime number")
