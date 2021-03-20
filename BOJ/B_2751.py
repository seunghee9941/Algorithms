import sys

N = int(sys.stdin.readline())
num = []

for _ in range(N):
    num.append(int(sys.stdin.readline()))

for n in sorted(num):
    print(n)