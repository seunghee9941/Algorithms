import sys

stack = []
op = []
count = 1
result = True

N = int(sys.stdin.readline())
for _ in range(N):
    n = int(sys.stdin.readline())
    while count <= n:
        stack.append(count)
        op.append('+')
        count += 1
    if stack[-1] == n:
        stack.pop()
        op.append('-')
    else:
        result = False

if result is False:
    print('NO')
else:
    print("\n".join(op))