import math

'''
Napisać program który policzy pole powierzchni oraz obwód, bazując na zmiennych jakie poda użytkownik:
Koła 
Kwadratu 
Prostokąta 
Trójkąta 
'''

print("This program will calculate the area and circumference of the figure chosen by you.")
print("a length: \n")
a = int(input())
print("b length: \n")
b = int(input())
print("Choose the figure by writing the corresponding number" +
      " 1 - square" +
      " 2 - rectangle" +
      " 3 - circle" +
      " 4 -triangle"
      )
choice = int(input())
if (choice == 1):
    circumference = 4 * a
    area = a ** 2
    print("Square area is: ", area, " Square circumference is: ", circumference)
elif (choice == 2):
    circumference = 2 * a + 2 * b
    area = a * b
    print("Rectangle area is: ", area, " Rectangle circumference is: ", circumference)
elif (choice == 3):
    diagonal = a / 2
    area = math.pi * diagonal ** 2
    circumference = 2 * math.pi * diagonal
    print("Circle area is: ", area, "Circle circumference is: ", circumference)
elif (choice == 4):
    area = (a * b) / 2
    c = a ** 2 + b ** 2
    c = math.sqrt(c)
    circumference = a + b + c
    print("Triangle area is: ", area, "Triangle circumference is: ", circumference)
else:
    print("Your choice doesn't correspond with any of the above figures")
