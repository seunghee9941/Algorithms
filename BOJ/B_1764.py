N, M = map(int, input().split())
N_name = set()
M_name = set()

for i in range(N):
    N_name.add(input())
for i in range(M):
    M_name.add(input())

name = sorted(list(N_name & M_name))

print(len(name))
for n in sorted(name):
    print(n)
