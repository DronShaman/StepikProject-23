n = int(input())
zap = []
rez = []

for i in range(0, n):
    m = input()
    zap.append(m)
new = input()

for i in range(0, n):
    if new in zap[i] or new.title() in zap[i] or new.lower() in zap[i] or new.upper() in zap[i] or new.swapcase() in zap[i] or new.capitalize() in zap[i]:
        print(zap[i])