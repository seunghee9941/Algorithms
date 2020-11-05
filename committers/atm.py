n = int(input())

times = list(map(int, input().split()))
times.sort()
time_sum = 0

for i in range(n):
    time_sum += times[i]*(n-i)

print(time_sum)
