nums = input().split('-')

sum = 0
for i in nums[0].split('+'):
    sum += int(i)

for i in nums[1:]:
    for j in i.split('+'):
        sum -= int(j)

print(sum)
