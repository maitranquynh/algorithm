def fourSumCount(A, B, C, D):
    firstPairs = {}
    res = 0
    for a in A:
        for b in B:
            if a + b in firstPairs:
                firstPairs[a+b] += 1;
            else:
                firstPairs[a+b] = 1;

    for c in C:
        for d in D:
                if -(c + d) in firstPairs:
                    res += firstPairs[-(c + d)]

    return res

A = [-1,1,1,1,-1]
B = [0,-1,-1,0,1]
C = [-1,-1,1,-1,-1]
D = [0,1,0,-1,-1]

print(fourSumCount(A, B, C, D))