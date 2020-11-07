A,B,V = map(int, input().split())
m = V - B

if m % (A-B) == 0:
    day = int(m/(A-B))
else:
    day = int(m/(A-B)+1)

print(day)
