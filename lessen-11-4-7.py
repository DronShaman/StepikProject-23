n = int(input())
zap = []
rez = []
z = []

for i in range(0, n):
    m = input()
    zap.append(m)
k = int(input())
for j in range(0, k):
    s = input()
    rez.append(s)

for i in range(0, n):
    for g in range(0, k):
        if rez[g].lower() in zap[i].lower():
            z.append(zap[i])

z = list(set(z))
for i in range(0, len(z)):
    print(z[i])