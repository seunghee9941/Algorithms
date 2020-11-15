T = int(input())

for i in range(T):
    R,S = input().split()
    P = ''
    for j in range(len(S)):
        P += int(R)*S[j]
    print(P)
