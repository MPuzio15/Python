n=5
for x in range(1,n+1,1):
    for j in range(1, x+1,1):
        if j==x:
            print(j)
        else:
            print(j, end="+")
    print()