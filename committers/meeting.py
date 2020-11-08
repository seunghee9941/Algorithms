N = int(input())

I = []
for i in range(N):
    s, e = map(int, input().split())
    I.append([s, e])

I = sorted(I, key=lambda I:(I[1],I[0]))

cnt = 1
end = I[0][1]

for i in range(1,len(I)):
    if I[i][0] >= end:
        cnt += 1
        end = I[i][1]

print(cnt)
