import sys

N = int(sys.stdin.readline())
km = list(map(int, sys.stdin.readline().split()))
won = list(map(int, sys.stdin.readline().split()))

cost = 0
min_cost = won[0]

for i in range(N-1):
    if won[i] <= min_cost:
        min_cost = won[i]
    cost += min_cost*km[i]

print(cost)