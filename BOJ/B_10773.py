import sys

K = int(sys.stdin.readline())
money = []

for _ in range(K):
    m = int(sys.stdin.readline())
    if (m != 0):
        money.append(m)
    else: money.pop()

m_sum = 0
for i in range(len(money)):
    m_sum += money[i]
    
print(m_sum)
