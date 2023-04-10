n = int(input())
zap = []
rez = []

for i in range(0, n):
    m = input()
    zap.append(m)
new = input()

for i in range(0, n):
    if new.lower() in zap[i].lower():
        print(zap[i])