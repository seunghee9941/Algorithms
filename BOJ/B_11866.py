import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
queue = deque([i for i in range(1, N+1)])
result = []

while queue:
    queue.rotate(-(K-1))
    result.append(queue.popleft())

print("<"+", ".join(list(map(str, result)))+">")