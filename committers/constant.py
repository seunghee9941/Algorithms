[A, B] = map(str, input().split())

rA = ''.join(reversed(A))
rB = ''.join(reversed(B))

if(int(rA)>int(rB)): print(rA)
elif (int(rA)<int(rB)): print(rB)
