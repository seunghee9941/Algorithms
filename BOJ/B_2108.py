import sys
from collections import Counter

N = int(sys.stdin.readline())
nums = []

for _ in range(N):
    nums.append(int(sys.stdin.readline()))
    
cnums = Counter(sorted(nums)).most_common()

# 산술평균
print(round(sum(nums)/len(nums)))

# 중앙값
print(sorted(nums)[(len(nums)//2)])

# 최빈값
if len(cnums) > 1:
    if cnums[0][1] == cnums[1][1]: print(cnums[1][0])
    else: print(cnums[0][0])
else: print(nums[0])

# 범위
print(max(nums)-min(nums))
