'''
zad 5
Napisać program który wyświetli numeryczny trójkąt dla podanej przez użytkownika liczby
print("Podaj liczbe calkowita dodatnia: ")
'''
number = int(input("Provide a positive number: "))
for i in range(1, number+1):
    for j in range(1, i+1 ):
        if j==i:
            print(j)
        else:
            print(j, end = ", ")

#christmas tree

