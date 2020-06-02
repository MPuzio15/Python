'''
Napisać program, który zapyta użytkownika o pozytywną liczbę całkowitą: 'N'
a następnie wypisze potęgi wszystkich liczb od 1 do N: =>5 >>1 >>4 >>9 >>16 >>25
'''

print("Provide the positive number: ")
number = int(input())
for i in range(1, number+1):
    print(i**2)
    i+=1
