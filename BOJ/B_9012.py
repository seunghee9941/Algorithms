import sys

T = int(sys.stdin.readline())

for _ in range(T):
    PS = []
    S = sys.stdin.readline().rstrip()
    close = False
    
    for s in S:
        if (s == "("):
            PS.append("(")
        elif (s == ")"):
            if not PS:
                print("NO")
                close = True
                break
            else: PS.pop()
            
    if close == True: continue
    if not PS: print("YES")
    else: print("NO")
