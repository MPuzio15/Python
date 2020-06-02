'''
Załóżmy ze mamy nie pustą listę intigerów np. a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 23, 26].
Napisz kod który wypisze wszystkie elementy mniejsze od 24
'''
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 23, 26]
b=[]
for i in range(len(a)):
    if(a[i]<24):
        b.append(a[i])
print(b)