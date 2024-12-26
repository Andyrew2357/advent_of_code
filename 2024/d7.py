from collections import deque

s1 = 0

with open('d7_in.txt', 'r') as f:
    for l in f.readlines():
        K, X = l.split(':')
        K = int(K)
        X = [int(s) for s in X.split()]
        S = [X[0]]
        for x in X[1:]: 
            A = [s*x for s in S]
            B = [s+x for s in S]
            S = A+B

        if K in S: s1+=K

print(s1)

s2 = 0

with open('d7_in.txt', 'r') as f:
    for l in f.readlines():
        K, X = l.split(':')
        K = int(K)
        X = [int(s) for s in X.split()]
        S = [X[0]]
        for x in X[1:]: 
            A = [s*x for s in S]
            B = [s+x for s in S]
            C = [int(str(s)+str(x)) for s in S]
            S = A+B+C

        if K in S: s2+=K

print(s2)
