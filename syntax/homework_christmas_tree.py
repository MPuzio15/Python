number = int(input("Provide a positive number: "))

for i in range(1, number+1):
    for j in range(1,i+1):
        if(i == j):
            print("#")
        else:
            print("#", end='')