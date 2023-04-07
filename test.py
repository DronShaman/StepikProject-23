d = [input() for _ in range(int(input()))]
query = input()
[print(s) for s in d if query.lower() in s.lower()]