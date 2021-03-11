import sys

N, M = map(int, sys.stdin.readline().split())
N_name = set()
M_name = set()

for _ in range(N):
    N_name.add(sys.stdin.readline().rstrip())
for _ in range(M):
    M_name.add(sys.stdin.readline().rstrip())

name = sorted(list(N_name & M_name))

print(len(name))
for n in sorted(name):
    print(n)
