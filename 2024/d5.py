from collections import defaultdict
from functools import cmp_to_key

with open('d5_in.txt', 'r') as f:
    rul = defaultdict(list)

    while True:
        l = f.readline()
        if l == '\n': break
        a, b = (int(s) for s in l.strip().split('|'))
        rul[a].append(b)

    def cmp(a, b):
        return -1 if b in rul[a] else 1

    def valid(A):
        for i in range(len(A)-1):
            if not all(j in rul[A[i]] for j in A[i+1:]): return False
        return True

    s1 = 0
    s2 = 0
    for l in f.readlines():
        A = [int(s) for s in l.strip().split(',')]
        if valid(A): 
            s1+=A[len(A)//2]
        else:
            A.sort(key=cmp_to_key(cmp))
            s2+=A[len(A)//2]

    print(s1)
    print(s2)
