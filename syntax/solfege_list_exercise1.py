solfege = ["do", "re", "mi", "fa", "sol", "la", "si", "Do"]

print(solfege)
for a,b in list(enumerate(solfege)):
    print(a,b)
for i, v in reversed(list(enumerate(solfege))):
    print(i, v)

print(solfege[::1])

C = [solfege[0], solfege[2], solfege[4]]
print("C: ", C)
G = [solfege[-2], solfege[1], solfege[4]]
print("G: ", G)
e = [solfege[-2], solfege[1], solfege[4]]
print("e: ", e)

cat=[4,2,2,3,1,1,0,2,4,0,2,4,4,2,2,3,0,1,0,2,0,0,2,0]

for i in range(len(cat)):
    note = cat[i]
    play = solfege[note]
    print(play)

G = [2,1,4]
for i in range(len(G)):
    note = G[i]
    play = solfege[note]
    print(play)
