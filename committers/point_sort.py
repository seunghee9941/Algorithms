n = int(input())

points = []
for i in range(n):
    [x, y] = map(int, input().split())
    arr = [y, x]
    points.append(arr)

points = sorted(points)

for i in range(n):
    print(points[i][1], points[i][0])
